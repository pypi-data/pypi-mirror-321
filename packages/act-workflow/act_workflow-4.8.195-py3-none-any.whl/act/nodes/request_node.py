import json
import logging
import requests
from typing import Dict, Any, Union, Optional, List, Tuple
from .base_node_prod import BaseNode, NodeSchema, NodeParameter, NodeParameterType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RequestNode(BaseNode):
    """HTTP Request Node with enhanced schema validation."""

    def get_schema(self) -> NodeSchema:
        """Define the schema for Request node."""
        return NodeSchema(
            node_type="request",
            version="1.0.0",
            description="Node for making HTTP requests",
            parameters=[
                NodeParameter(
                    name="url",
                    type=NodeParameterType.STRING,
                    description="URL to send the request to",
                    required=True,
                    pattern=r"^https?://.+"
                ),
                NodeParameter(
                    name="method",
                    type=NodeParameterType.STRING,
                    description="HTTP method",
                    required=True,
                    enum=["GET", "POST", "PUT", "DELETE", "PATCH"]
                ),
                NodeParameter(
                    name="headers",
                    type=NodeParameterType.STRING,
                    description="Request headers as JSON string",
                    required=False,
                    default="{}"
                ),
                NodeParameter(
                    name="params",
                    type=NodeParameterType.STRING,
                    description="Query parameters as JSON string",
                    required=False,
                    default="{}"
                ),
                NodeParameter(
                    name="body",
                    type=NodeParameterType.STRING,
                    description="Request body as JSON string",
                    required=False
                ),
                NodeParameter(
                    name="timeout",
                    type=NodeParameterType.NUMBER,
                    description="Request timeout in seconds",
                    required=False,
                    default=30,
                    min_value=1,
                    max_value=300
                ),
                NodeParameter(
                    name="output_field",
                    type=NodeParameterType.STRING,
                    description="Field name for the output",
                    required=False,
                    default="response"
                )
            ],
            outputs={
                "status_code": NodeParameterType.NUMBER,
                "headers": NodeParameterType.OBJECT,
                "body": NodeParameterType.OBJECT
            }
        )

    def _validate_input(self, node_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate input data against schema.
        Returns tuple of (is_valid, list_of_errors)
        """
        errors = []
        schema = self.get_schema()

        # Check for missing required parameters
        for param in schema.parameters:
            if param.required and param.name not in node_data:
                errors.append(f"Missing required parameter: '{param.name}' ({param.description})")
                continue

            if param.name in node_data:
                value = node_data[param.name]
                
                # Validate enum values
                if param.enum and value not in param.enum:
                    errors.append(
                        f"Invalid value for '{param.name}': '{value}'. "
                        f"Must be one of: {', '.join(param.enum)}"
                    )

                # Validate numeric ranges
                if param.type == NodeParameterType.NUMBER:
                    try:
                        num_value = float(value)
                        if param.min_value is not None and num_value < param.min_value:
                            errors.append(
                                f"Value for '{param.name}' must be >= {param.min_value}"
                            )
                        if param.max_value is not None and num_value > param.max_value:
                            errors.append(
                                f"Value for '{param.name}' must be <= {param.max_value}"
                            )
                    except (ValueError, TypeError):
                        errors.append(f"Value for '{param.name}' must be a number")

                # Validate URL pattern
                if param.pattern and param.type == NodeParameterType.STRING:
                    import re
                    if not re.match(param.pattern, str(value)):
                        errors.append(
                            f"Value for '{param.name}' does not match required pattern"
                        )

        return len(errors) == 0, errors

    def _parse_json_field(self, field_data: Any, field_name: str) -> Dict:
        """Parse a JSON string field or return empty dict if None."""
        if not field_data:
            return {}
        
        if isinstance(field_data, dict):
            return field_data
            
        try:
            if isinstance(field_data, str):
                return json.loads(field_data)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing {field_name}: {str(e)}")
            return {}
        
        return {}

    def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute HTTP request with enhanced validation."""
        try:
            logger.info("Executing RequestNode...")

            # Validate input against schema
            is_valid, errors = self._validate_input(node_data)
            if not is_valid:
                error_message = "\n".join(errors)
                logger.error(f"Validation errors:\n{error_message}")
                return {
                    "status": "error",
                    "message": "Validation failed",
                    "errors": errors
                }

            # Extract and clean base parameters
            method = str(node_data.get("method", "GET")).upper()
            url = str(node_data.get("url", "")).strip()
            timeout = int(float(str(node_data.get("timeout", "30")).strip()))
            output_field = str(node_data.get("output_field", "response")).strip()

            # Parse JSON string fields
            headers = self._parse_json_field(node_data.get("headers"), "headers")
            params = self._parse_json_field(node_data.get("params"), "params")
            body = self._parse_json_field(node_data.get("body"), "body")

            # Execute request
            try:
                logger.info(f"Sending {method} request to {url}")
                logger.debug(f"Headers: {headers}, Params: {params}, Body: {body}")
                
                response = self._make_request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    body=body,
                    timeout=timeout
                )

                # Process response
                result = {
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "body": self._parse_response_body(response)
                }

                # Return based on status code
                if 200 <= response.status_code < 300:
                    return {
                        "status": "success",
                        "message": f"Request completed successfully with status {response.status_code}",
                        "result": {
                            output_field: result
                        }
                    }
                else:
                    return {
                        "status": "error",
                        "message": f"Request failed with status {response.status_code}",
                        "details": f"The {method} method might not be supported by this endpoint",
                        "result": {
                            output_field: result
                        }
                    }

            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {str(e)}")
                return self.handle_error(e, "Request execution")

        except Exception as e:
            logger.error(f"Error in RequestNode execution: {str(e)}")
            return self.handle_error(e, "RequestNode execution")

    def _make_request(
        self,
        method: str,
        url: str,
        headers: Dict[str, str],
        params: Dict[str, Any],
        body: Optional[Dict[str, Any]],
        timeout: int
    ) -> requests.Response:
        """Send an HTTP request."""
        request_kwargs = {
            "url": url,
            "headers": headers,
            "params": params,
            "timeout": timeout
        }

        if method in ["POST", "PUT", "PATCH"] and body is not None:
            request_kwargs["json"] = body

        return requests.request(method=method, **request_kwargs)

    def _parse_response_body(self, response: requests.Response) -> Union[Dict[str, Any], str]:
        """Parse response body as JSON if possible."""
        try:
            return response.json()
        except json.JSONDecodeError:
            return response.text

# Example usage
if __name__ == "__main__":
    # Test data with missing required parameter
    test_data = {
        "url": "https://httpbin.org/post",
        # method is missing
        "headers": '{"Content-Type": "application/json"}',
        "body": '{"message": "Test request"}',
        "output_field": "http_response"
    }

    node = RequestNode()
    result = node.execute(test_data)
    print(json.dumps(result, indent=2))