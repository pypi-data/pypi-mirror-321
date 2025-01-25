import json
import logging
import requests
from typing import Dict, Any, Union
from .base_node_prod import BaseNode

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class RequestNode(BaseNode):
   def execute(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
       """
       Executes an HTTP request based on the provided configuration.
       """
       try:
           logger.info("Executing RequestNode...")

           # Clean and validate required parameters
           method = str(node_data.get("method", "GET")).strip('"\'').upper()
           url = str(node_data.get("url", "")).strip('"\'')
           headers = self._clean_dict(node_data.get("headers", {}))
           params = self._clean_dict(node_data.get("params", {}))
           body = self._clean_dict(node_data.get("body"))
           timeout = int(str(node_data.get("timeout", 30)).strip('"\''))
           output_field = str(node_data.get("output_field", "response")).strip('"\'')

           # Validate parameters
           if not url:
               return {"status": "error", "message": "Missing required parameter 'url'"}

           supported_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
           if method not in supported_methods:
               return {"status": "error", "message": f"Unsupported HTTP method: {method}. Supported methods: {', '.join(supported_methods)}"}

           # Execute request
           try:
               logger.info(f"Sending {method} request to {url}")
               logger.debug(f"Request details: headers={headers}, params={params}, body={body}")

               response = self._make_request(
                   method=method,
                   url=url, 
                   headers=headers,
                   params=params,
                   body=body,
                   timeout=timeout
               )

               # Build result with response details
               result = {
                   "status_code": response.status_code,
                   "headers": dict(response.headers),
                   "body": self._parse_response_body(response)
               }

               # Determine success based on status code
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
                       "result": {
                           output_field: result
                       }
                   }

           except requests.exceptions.RequestException as e:
               logger.error(f"Request failed: {str(e)}")
               return {
                   "status": "error",
                   "message": f"Request failed: {str(e)}"
               }

       except Exception as e:
           logger.error(f"Error in RequestNode execution: {str(e)}")
           return {
               "status": "error",
               "message": str(e)
           }

   def _make_request(
       self,
       method: str,
       url: str,
       headers: Dict[str, str],
       params: Dict[str, Any],
       body: Union[Dict[str, Any], None],
       timeout: int
   ) -> requests.Response:
       """Sends an HTTP request using the requests library."""
       request_kwargs = {
           "url": url,
           "headers": headers,
           "params": params,
           "timeout": timeout
       }

       # Add body for appropriate methods
       if method in ["POST", "PUT", "PATCH"] and body is not None:
           request_kwargs["json"] = body

       return requests.request(method=method, **request_kwargs)

   def _parse_response_body(self, response: requests.Response) -> Union[Dict[str, Any], str]:
       """Parses the response body as JSON if possible, otherwise returns text."""
       try:
           return response.json()
       except json.JSONDecodeError:
           return response.text

   def _clean_dict(self, data: Union[Dict[str, Any], None]) -> Union[Dict[str, Any], None]:
       """Clean string values in a dictionary, removing quotes."""
       if not isinstance(data, dict):
           return data
           
       cleaned = {}
       for key, value in data.items():
           # Clean key
           clean_key = key.strip('"\'') if isinstance(key, str) else key
           
           # Clean value recursively
           if isinstance(value, dict):
               clean_value = self._clean_dict(value)
           elif isinstance(value, str):
               clean_value = value.strip('"\'')
           elif isinstance(value, list):
               clean_value = [
                   self._clean_dict(item) if isinstance(item, dict)
                   else item.strip('"\'') if isinstance(item, str)
                   else item
                   for item in value
               ]
           else:
               clean_value = value
               
           cleaned[clean_key] = clean_value
           
       return cleaned

if __name__ == "__main__":
   # Example usage
   request_node = RequestNode()
   test_data = {
       "method": "POST",
       "url": "https://httpbin.org/post",
       "headers": {
           "Content-Type": "application/json",
           "Accept": "application/json"
       },
       "body": {
           "message": "Test request"
       },
       "output_field": "http_response"
   }
   result = request_node.execute(test_data)
   print(json.dumps(result, indent=2))