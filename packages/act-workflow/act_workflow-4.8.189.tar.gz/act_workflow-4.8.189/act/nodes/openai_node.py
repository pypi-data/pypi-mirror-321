import logging
import json


class OpenAINode:
    def __init__(self):
        self.outputs = {}

    def execute(self, node_data):
        """
        Execute the OpenAINode functionality.

        Parameters:
        - node_data: A dictionary containing node-specific data, such as
                     api_key, input_text, model, and output_field.

        Returns:
        - A dictionary containing the status, message, and result of the execution.
        """
        try:
            # Extract parameters from node_data
            api_key = node_data.get("api_key")
            input_text = node_data.get("input_text", "")
            model = node_data.get("model", "gpt-4")
            output_field = node_data.get("output_field")

            # Validate required parameters
            if not api_key:
                raise ValueError("API key is missing.")
            if not input_text:
                raise ValueError("Input text is missing.")
            if not output_field:
                raise ValueError("Output field is not specified.")

            # Simulate OpenAI API call (replace with actual API integration)
            response = self.call_openai_api(api_key, model, input_text)

            # Process response to extract JSON data
            raw_text = response.get("choices", [{}])[0].get("text", "").strip()
            json_data = self.extract_json_from_text(raw_text)

            if not json_data:
                raise ValueError("No valid JSON object found in the OpenAI response.")

            # Set output for the current node
            self.outputs[output_field] = json_data

            return {
                "status": "success",
                "message": "OpenAI API call succeeded",
                "result": {output_field: json_data},
            }
        except Exception as e:
            logging.error(f"Error in OpenAINode execution: {e}")
            return {"status": "error", "message": str(e)}

    def call_openai_api(self, api_key, model, input_text):
        """
        Simulates a call to the OpenAI API. Replace this with the actual API integration.

        Parameters:
        - api_key: The OpenAI API key.
        - model: The model to use (e.g., "gpt-4").
        - input_text: The prompt or input text for the API.

        Returns:
        - A simulated response in dictionary format.
        """
        logging.info(f"Calling OpenAI API with model: {model}")
        # Simulated response (replace this with actual OpenAI API call)
        return {
            "choices": [
                {
                    "text": """
                    {
                        "value1": "Hello, World!",
                        "value2": 123456,
                        "value3": {
                            "subKey1": "This is a nested value",
                            "subKey2": true
                        }
                    }
                    """
                }
            ]
        }

    def extract_json_from_text(self, raw_text):
        """
        Extract JSON data from a text response.

        Parameters:
        - raw_text: The raw text returned by the OpenAI API.

        Returns:
        - A dictionary containing the parsed JSON object, or None if no valid JSON was found.
        """
        try:
            # Locate JSON object in the text
            json_start = raw_text.find("{")
            json_end = raw_text.rfind("}") + 1

            if json_start == -1 or json_end == -1:
                return None

            # Parse JSON
            json_data = raw_text[json_start:json_end]
            return json.loads(json_data)
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return None
