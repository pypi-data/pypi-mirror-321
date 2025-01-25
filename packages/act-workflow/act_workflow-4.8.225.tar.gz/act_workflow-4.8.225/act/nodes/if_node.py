import logging


class IfNode:
    def __init__(self):
        self.outputs = {}

    def execute(self, node_data):
        """
        Execute the IfNode functionality.

        Parameters:
        - node_data: A dictionary containing node-specific data, such as
                     condition, true_path, false_path, and input.

        Returns:
        - A dictionary containing the status, message, and result of the execution.
        """
        try:
            # Extract parameters from node_data
            condition = node_data.get("condition", "")
            true_path = node_data.get("true_path")
            false_path = node_data.get("false_path")
            input_data = node_data.get("input", {}).get("result", {})

            # Validate required parameters
            if not condition:
                raise ValueError("Condition is missing.")
            if not true_path or not false_path:
                raise ValueError("Both true_path and false_path must be specified.")

            # Resolve placeholders in the condition
            resolved_condition = self.resolve_placeholders(condition, input_data)

            logging.info(f"Resolved condition: {resolved_condition}")

            # Evaluate the resolved condition
            condition_result = eval(resolved_condition)  # Use a safe evaluation approach in production

            # Determine the next path
            next_path = true_path if condition_result else false_path

            self.outputs["next_path"] = next_path
            return {
                "status": "success",
                "message": f"IfNode executed successfully, taking {'true' if condition_result else 'false'} path",
                "result": {
                    "next_path": next_path,
                    "evaluated_condition": condition_result,
                },
            }
        except Exception as e:
            logging.error(f"Error in IfNode execution: {e}")
            return {"status": "error", "message": str(e)}

    def resolve_placeholders(self, condition, data):
        """
        Resolve placeholders in the condition string using the input data.

        Parameters:
        - condition: The condition string containing placeholders.
        - data: The data dictionary to resolve placeholders against.

        Returns:
        - The resolved condition string.
        """
        try:
            while "{{" in condition and "}}" in condition:
                start = condition.index("{{") + 2
                end = condition.index("}}")
                placeholder = condition[start:end].strip()

                # Resolve the placeholder using the data dictionary
                value = self.get_nested_value(data, placeholder.split("."))
                if isinstance(value, str):
                    value = f"'{value}'"  # Ensure string values are quoted
                condition = condition.replace(f"{{{{{placeholder}}}}}", str(value))

            return condition
        except Exception as e:
            logging.error(f"Error resolving placeholders: {e}")
            raise ValueError(f"Invalid placeholder resolution: {e}")

    def get_nested_value(self, data, keys):
        """
        Retrieve a nested value from a dictionary using a list of keys.

        Parameters:
        - data: The dictionary to search.
        - keys: A list of keys representing the path to the value.

        Returns:
        - The value at the specified path, or None if not found.
        """
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return None
        return data
