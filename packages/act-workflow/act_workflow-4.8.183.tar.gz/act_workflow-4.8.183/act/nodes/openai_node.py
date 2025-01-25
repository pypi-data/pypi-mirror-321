import logging
import json
from typing import Dict, Any, Optional
import openai
from .base_node import BaseNode

class OpenAINode(BaseNode):
    """
    Node for interacting with OpenAI API with support for different operations.
    Operations supported:
    - chat: Send chat completion request
    - completion: Send text completion request
    - embedding: Generate embeddings
    """
    
    def __init__(self, sandbox_timeout: Optional[int] = None):
        super().__init__(sandbox_timeout)
        self.outputs = {}
        self.supported_operations = {
            'chat': self._execute_chat,
            'completion': self._execute_completion,
            'embedding': self._execute_embedding
        }

    def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the OpenAI node with specified operation.
        
        Expected node_data format:
        {
            "operation": "chat|completion|embedding",
            "params": {
                "api_key": "your-api-key",
                "model": "gpt-4",
                "input_text": "Your prompt",
                "output_field": "result_field",
                ... operation-specific parameters ...
            }
        }
        """
        try:
            # Validate basic requirements
            self.validate_params(["api_key", "input_text", "output_field", "operation"], node_data.get("params", {}))
            
            # Extract parameters
            params = node_data.get("params", {})
            operation = params.get("operation")
            
            # Set up OpenAI client
            openai.api_key = params.get("api_key")
            
            # Check if operation is supported
            if operation not in self.supported_operations:
                raise ValueError(f"Unsupported operation: {operation}")
            
            # Execute the specified operation
            result = self.supported_operations[operation](params)
            
            # Store output
            output_field = params.get("output_field")
            self.outputs[output_field] = result
            
            return {
                "status": "success",
                "message": f"OpenAI {operation} operation succeeded",
                "result": {output_field: result}
            }
            
        except Exception as e:
            return self.handle_error(e, context=f"OpenAINode {operation} operation")

    def _execute_chat(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute chat completion operation"""
        messages = self._prepare_chat_messages(params.get("input_text"))
        model = params.get("model", "gpt-4")
        
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=params.get("temperature", 0.7),
            max_tokens=params.get("max_tokens", 1000)
        )
        
        return self._process_chat_response(response)

    def _execute_completion(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute text completion operation"""
        model = params.get("model", "text-davinci-003")
        
        response = openai.Completion.create(
            model=model,
            prompt=params.get("input_text"),
            temperature=params.get("temperature", 0.7),
            max_tokens=params.get("max_tokens", 1000)
        )
        
        return self._process_completion_response(response)

    def _execute_embedding(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute embedding operation"""
        model = params.get("model", "text-embedding-ada-002")
        
        response = openai.Embedding.create(
            model=model,
            input=params.get("input_text")
        )
        
        return self._process_embedding_response(response)

    def _prepare_chat_messages(self, input_text: str) -> list:
        """Prepare messages for chat completion"""
        if isinstance(input_text, str):
            messages = [{"role": "user", "content": input_text}]
        elif isinstance(input_text, list):
            messages = input_text
        else:
            raise ValueError("input_text must be either a string or a list of messages")
        return messages

    def _process_chat_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Process chat completion response"""
        try:
            message = response['choices'][0]['message']
            return {
                "content": message['content'],
                "role": message['role'],
                "finish_reason": response['choices'][0]['finish_reason']
            }
        except (KeyError, IndexError) as e:
            raise ValueError(f"Invalid response format from OpenAI API: {e}")

    def _process_completion_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Process text completion response"""
        try:
            return {
                "text": response['choices'][0]['text'],
                "finish_reason": response['choices'][0]['finish_reason']
            }
        except (KeyError, IndexError) as e:
            raise ValueError(f"Invalid response format from OpenAI API: {e}")

    def _process_embedding_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """Process embedding response"""
        try:
            return {
                "embedding": response['data'][0]['embedding'],
                "model": response['model']
            }
        except (KeyError, IndexError) as e:
            raise ValueError(f"Invalid response format from OpenAI API: {e}")