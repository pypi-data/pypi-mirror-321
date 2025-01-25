import os
import json
import logging
from typing import Dict, Any, Optional, List
from enum import Enum
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, validator
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class NodeParameterType(str, Enum):
    """Enum defining possible parameter types for node inputs."""
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    SECRET = "secret"

class NodeParameter(BaseModel):
    """Defines a single parameter for a node."""
    name: str
    type: NodeParameterType
    description: str
    required: bool = True
    default: Optional[Any] = None
    enum: Optional[List[Any]] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    pattern: Optional[str] = None

    @validator('default')
    def validate_default_value(cls, v, values):
        if v is not None:
            param_type = values.get('type')
            if param_type == NodeParameterType.STRING and not isinstance(v, str):
                raise ValueError("Default value must be a string")
            elif param_type == NodeParameterType.NUMBER and not isinstance(v, (int, float)):
                raise ValueError("Default value must be a number")
            elif param_type == NodeParameterType.BOOLEAN and not isinstance(v, bool):
                raise ValueError("Default value must be a boolean")
        return v

class NodeSchema(BaseModel):
    """Base schema definition for a node."""
    node_type: str
    version: str
    description: str
    parameters: List[NodeParameter]
    outputs: Dict[str, NodeParameterType]

class BaseNode(ABC):
    """Enhanced base node with schema support."""
    
    def __init__(self, sandbox_timeout: Optional[int] = None):
        """Initialize the base node."""
        logger.info("Initializing BaseNode")
        self.sandbox_timeout = sandbox_timeout
        self._schema = self.get_schema()

    @abstractmethod
    def get_schema(self) -> NodeSchema:
        """Return the schema definition for this node."""
        pass

    def validate_schema(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate input data against the node's schema.
        :param node_data: The input data to validate
        :return: Validated and processed data
        """
        validated_data = {}
        params = node_data.get("params", {})

        try:
            for param in self._schema.parameters:
                value = params.get(param.name)

                # Handle required parameters
                if param.required and value is None:
                    raise ValueError(f"Missing required parameter: {param.name}")

                # Apply default value if needed
                if value is None and param.default is not None:
                    value = param.default

                # Skip if no value and not required
                if value is None and not param.required:
                    continue

                # Type validation
                self._validate_type(param, value)

                # Range validation for numbers
                if param.type == NodeParameterType.NUMBER:
                    self._validate_range(param, value)

                # Enum validation
                if param.enum is not None and value not in param.enum:
                    raise ValueError(f"Parameter {param.name} must be one of: {param.enum}")

                # Pattern validation for strings
                if param.pattern is not None and param.type == NodeParameterType.STRING:
                    if not re.match(param.pattern, value):
                        raise ValueError(f"Parameter {param.name} does not match required pattern")

                validated_data[param.name] = value

            return validated_data

        except Exception as e:
            raise ValueError(f"Schema validation error: {str(e)}")

    def _validate_type(self, param: NodeParameter, value: Any):
        """Validate parameter type."""
        if param.type == NodeParameterType.STRING and not isinstance(value, str):
            raise ValueError(f"Parameter {param.name} must be a string")
        elif param.type == NodeParameterType.NUMBER and not isinstance(value, (int, float)):
            raise ValueError(f"Parameter {param.name} must be a number")
        elif param.type == NodeParameterType.BOOLEAN and not isinstance(value, bool):
            raise ValueError(f"Parameter {param.name} must be a boolean")
        elif param.type == NodeParameterType.ARRAY and not isinstance(value, list):
            raise ValueError(f"Parameter {param.name} must be an array")
        elif param.type == NodeParameterType.OBJECT and not isinstance(value, dict):
            raise ValueError(f"Parameter {param.name} must be an object")

    def _validate_range(self, param: NodeParameter, value: Any):
        """Validate numeric range."""
        if param.min_value is not None and value < param.min_value:
            raise ValueError(f"Parameter {param.name} must be >= {param.min_value}")
        if param.max_value is not None and value > param.max_value:
            raise ValueError(f"Parameter {param.name} must be <= {param.max_value}")

    def validate_params(self, required_params: list, node_data: Dict[str, Any]) -> bool:
        """
        Legacy parameter validation method for backward compatibility.
        """
        missing_params = [param for param in required_params if param not in node_data.get("params", {})]
        if missing_params:
            error_message = f"Missing required parameters: {', '.join(missing_params)}"
            logger.error(error_message)
            raise ValueError(error_message)
        return True

    def resolve_placeholders(self, text: str, node_data: Dict[str, Any]) -> str:
        """Resolve placeholders in a string using the node_data context."""
        pattern = re.compile(r"\{\{(.*?)\}\}")
        matches = pattern.findall(text)

        for match in matches:
            parts = match.split('.')
            value = self.fetch_value(parts, node_data)
            if value is not None:
                text = text.replace(f"{{{{{match}}}}}", str(value))

        return text

    def fetch_value(self, path_parts: list, node_data: Dict[str, Any]) -> Any:
        """Fetch a value from the node_data using a list of keys."""
        value = node_data
        try:
            for part in path_parts:
                if isinstance(value, dict) and part in value:
                    value = value[part]
                else:
                    return None
            return value
        except Exception as e:
            logger.error(f"Error fetching value for path {'.'.join(path_parts)}: {e}")
            return None

    def extract_text(self, input_text: Any) -> str:
        """Extract actual text from input, handling JSON and other formats."""
        try:
            if isinstance(input_text, str):
                parsed = json.loads(input_text)
                if isinstance(parsed, dict):
                    return parsed.get('value', input_text)
            elif isinstance(input_text, dict):
                return input_text.get('value', str(input_text))
        except (json.JSONDecodeError, ValueError):
            pass
        return str(input_text)

    def log_safe_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Redact sensitive information from logs."""
        if isinstance(data, dict):
            return {k: ('[REDACTED]' if 'key' in k.lower() else v) for k, v in data.items()}
        return data

    def handle_error(self, error: Exception, context: str = "") -> Dict[str, Any]:
        """Handle an error and return a formatted error response."""
        error_message = f"Error in {context}: {str(error)}"
        logger.error(error_message)
        return {"status": "error", "message": error_message}

    @abstractmethod
    def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the node's main functionality."""
        pass

# Example implementation
class ExampleNode(BaseNode):
    def get_schema(self) -> NodeSchema:
        return NodeSchema(
            node_type="example",
            version="1.0.0",
            description="Example node that processes text with placeholders",
            parameters=[
                NodeParameter(
                    name="example_param",
                    type=NodeParameterType.STRING,
                    description="Input text with optional placeholders",
                    required=True
                )
            ],
            outputs={
                "processed_text": NodeParameterType.STRING
            }
        )

    def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Validate against schema
            validated_data = self.validate_schema(node_data)

            # Extract and process input text
            input_text = self.extract_text(validated_data["example_param"])
            logger.info(f"Processing input: {input_text}")

            # Resolve placeholders in text
            resolved_text = self.resolve_placeholders(input_text, node_data)
            logger.info(f"Resolved text: {resolved_text}")

            # Return success result
            return {
                "status": "success",
                "result": {
                    "processed_text": resolved_text
                }
            }

        except Exception as e:
            return self.handle_error(e, context="ExampleNode execution")

if __name__ == "__main__":
    # Test example node
    example_node = ExampleNode()
    
    # Print schema
    print("Node Schema:")
    print(example_node.get_schema().json(indent=2))
    
    # Test execution
    test_data = {
        "params": {
            "example_param": "Hello, {{user.name}}!"
        },
        "input": {
            "user": {
                "name": "Taj"
            }
        }
    }
    
    print("\nExecution Result:")
    result = example_node.execute(test_data)
    print(json.dumps(result, indent=2))