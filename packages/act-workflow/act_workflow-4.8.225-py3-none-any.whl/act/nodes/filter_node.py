import json
import logging
from typing import Dict, Any, List, Union, Callable
from .base_node_prod import BaseNode

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class FilterNode(BaseNode):
    def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the filter operation on the input data.
        """
        try:
            logger.info("Executing FilterNode...")
            logger.debug(f"Received node data: {node_data}")

            # Get input data and parameters
            input_data = self._get_input_data(node_data)
            filter_condition = str(node_data.get("filter_condition", "")).strip('"\'')
            output_field = str(node_data.get("output_field", "filtered_data")).strip('"\'')

            # Validate input data
            if not isinstance(input_data, list):
                if isinstance(input_data, dict):
                    input_data = [input_data]
                else:
                    return {
                        "status": "error",
                        "message": "'input_data' must be a list or a dictionary"
                    }

            # Check if we have a condition
            if not filter_condition:
                return {
                    "status": "error",
                    "message": "Filter condition is required"
                }

            # Apply filter using eval with item context
            filtered_data = []
            for item in input_data:
                try:
                    # Create evaluation context
                    eval_context = {
                        'item': item,
                        'True': True,
                        'False': False,
                        'None': None
                    }

                    # Replace placeholders in condition
                    condition = self._resolve_placeholders(filter_condition, item)
                    
                    # Evaluate condition
                    if eval(condition, {"__builtins__": {}}, eval_context):
                        filtered_data.append(item)
                except Exception as e:
                    logger.warning(f"Error evaluating condition for item {item}: {str(e)}")
                    continue

            logger.info(f"Filtering completed. {len(filtered_data)} items passed the filter.")
            return {
                "status": "success",
                "message": "Filtering completed successfully",
                "result": {
                    output_field: filtered_data
                }
            }

        except Exception as e:
            logger.error(f"Error in FilterNode execution: {str(e)}")
            return {
                "status": "error",
                "message": f"Error during filtering: {str(e)}"
            }

    def _get_input_data(self, node_data: Dict[str, Any]) -> Union[List[Any], Dict[str, Any]]:
        """Extract and process input data from node_data."""
        input_data = node_data.get("input_data", [])
        
        # Handle previous node's input if available
        previous_input = node_data.get("input", {})
        if previous_input and isinstance(previous_input, dict):
            previous_result = previous_input.get("result", {})
            if previous_result:
                if isinstance(input_data, str):
                    try:
                        input_data = json.loads(input_data.replace("'", '"'))
                    except json.JSONDecodeError:
                        input_data = [previous_result]
                elif not input_data or input_data == "[":  # Handle truncated TOML array
                    input_data = [previous_result]

        return input_data

    def _resolve_placeholders(self, condition: str, item: Dict[str, Any]) -> str:
        """Resolve placeholders in the condition using the item context."""
        def process_value(v):
            if isinstance(v, str):
                return f"'{v}'"
            return str(v)

        def replace_in_condition(cond, prefix, data):
            for k, v in data.items():
                placeholder = f"{{{{{prefix}.{k}}}}}"
                if placeholder in cond:
                    if isinstance(v, dict):
                        cond = replace_in_condition(cond, f"{prefix}.{k}", v)
                    else:
                        cond = cond.replace(placeholder, process_value(v))
            return cond

        if isinstance(item, dict):
            condition = replace_in_condition(condition, "item", item)

        return condition

if __name__ == "__main__":
    # Example usage
    filter_node = FilterNode()
    test_data = {
        "input_data": [
            {"id": 1, "value": 100},
            {"id": 2, "value": 50},
            {"id": 3, "value": 150}
        ],
        "filter_condition": "{{item.value}} > 100",
        "output_field": "filtered_data"
    }
    result = filter_node.execute(test_data)
    print(json.dumps(result, indent=2))