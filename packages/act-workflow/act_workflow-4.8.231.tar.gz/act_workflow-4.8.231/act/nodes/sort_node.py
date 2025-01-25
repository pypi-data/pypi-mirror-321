import json
import logging
from .base_node_prod import BaseNode

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class SortNode(BaseNode):
    def execute(self, node_data):
        """
        Sorts input data based on a specified field and order.
        Provides extensive logging and error handling.
        """
        logger.info("Executing SortNode...")
        logger.debug(f"Received node_data: {json.dumps(node_data, indent=2)}")

        # More comprehensive input validation and logging
        input_data = node_data.get("input_data", [])
        sort_field = node_data.get("sort_field")
        sort_order = node_data.get("sort_order", "asc").lower()
        output_field = node_data.get("output_field", "sorted_data")

        # Detailed logging for debugging
        logger.info(f"Input parameters:")
        logger.info(f"  - input_data type: {type(input_data)}")
        logger.info(f"  - sort_field: {sort_field}")
        logger.info(f"  - sort_order: {sort_order}")
        logger.info(f"  - output_field: {output_field}")

        # Attempt to infer sort_field if not provided
        if not sort_field and input_data:
            # If input_data is a list of dicts, try to use the first key
            if isinstance(input_data, list) and input_data and isinstance(input_data[0], dict):
                sort_field = list(input_data[0].keys())[0]
                logger.warning(f"No sort_field provided. Defaulting to first field: {sort_field}")

        # Validation with more informative errors
        if not isinstance(input_data, list):
            logger.error(f"input_data must be a list, got {type(input_data)}")
            return {
                "status": "error", 
                "message": f"'input_data' must be a list, not {type(input_data)}",
                "debug_info": {
                    "input_data_type": str(type(input_data)),
                    "input_data_repr": repr(input_data)
                }
            }

        if not input_data:
            logger.warning("Input data is empty")
            return {
                "status": "warning", 
                "message": "Input data is empty", 
                "result": {output_field: []}
            }

        if not sort_field:
            return {
                "status": "error", 
                "message": "Missing required parameter 'sort_field'",
                "debug_info": {
                    "available_keys": list(input_data[0].keys()) if input_data else []
                }
            }
        
        if sort_order not in ["asc", "desc"]:
            return {"status": "error", "message": "'sort_order' must be 'asc' or 'desc'"}

        try:
            sorted_data = self._sort_data(input_data, sort_field, sort_order)
            return {
                "status": "success",
                "message": "Sorting completed successfully",
                "result": {output_field: sorted_data}
            }
        except Exception as e:
            logger.error(f"Error during sorting: {e}")
            return {
                "status": "error", 
                "message": str(e),
                "debug_info": {
                    "sort_field": sort_field,
                    "input_data_sample": input_data[:2]  # Include first two items for context
                }
            }

    def _sort_data(self, data, field, order):
        """
        Sorts the data based on the specified field and order.
        Handles cases where the field might be missing in some dictionaries.
        """
        reverse = (order == "desc")
        
        def sort_key(x):
            # Return a default value if the field is not found
            # This prevents TypeError for missing or None values
            value = x.get(field)
            # Ensure consistent sorting by placing None/missing values last
            return (value is None, value)

        try:
            return sorted(data, key=sort_key, reverse=reverse)
        except TypeError as e:
            raise ValueError(f"Error sorting data by field '{field}': {e}")

if __name__ == "__main__":
    # Example usage with different scenarios
    sort_node = SortNode()
    
    # Test case 1: Normal sorting
    test_data1 = {
        "input_data": [
            {"id": 1, "name": "John", "age": 30},
            {"id": 2, "name": "Jane", "age": 25},
            {"id": 3, "name": "Doe", "age": 35}
        ],
        # Note: Intentionally removed sort_field to test error handling
        "sort_order": "desc",
        "output_field": "sorted_results"
    }
    result1 = sort_node.execute(test_data1)
    print("Test Case 1 (No Sort Field):")
    print(json.dumps(result1, indent=2))
    
    # Test case 2: Empty input
    test_data2 = {
        "input_data": [],
        "sort_field": "age",
        "sort_order": "desc",
        "output_field": "sorted_results"
    }
    result2 = sort_node.execute(test_data2)
    print("\nTest Case 2 (Empty Input):")
    print(json.dumps(result2, indent=2))