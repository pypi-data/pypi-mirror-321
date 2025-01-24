"""Perplexity API interaction module."""
import os
import json
import logging
from typing import Dict, Iterator, List, Optional, Any
import requests
from .config import LLAMA_MODELS

class PerplexityError(Exception):
    """Base exception for Perplexity-related errors."""
    pass

class APIError(PerplexityError):
    """API-related errors."""
    pass

class AuthenticationError(APIError):
    """Authentication-related errors."""
    pass

class PerplexityAPI:
    """Handle all Perplexity API interactions."""
    
    ENDPOINT = "https://api.perplexity.ai/chat/completions"
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("PERPLEXITY_API_KEY")
        log_level = logging.DEBUG if os.environ.get("PLEXSEARCH_DEBUG") else logging.INFO
        logging.basicConfig(level=log_level,
                          format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                          handlers=[
                              logging.StreamHandler(),
                              logging.FileHandler("plexsearch.log")
                          ])
        if not self.api_key:
            raise ValueError("API key required via argument or PERPLEXITY_API_KEY environment variable")
    
    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    # def _build_payload(self, query: str, model: str, stream: bool, show_citations: bool) -> Dict[str, any]:
    def _build_payload(self, query: str, model: str, stream: bool, show_citations: bool, context: Optional[List[Dict[str, str]]] = None) -> Dict[str, any]:
        # Convert model name if it's a short name
        if model in LLAMA_MODELS:
            model = LLAMA_MODELS[model]

        system_message = (
            "You are a technical assistant focused on providing accurate, practical "
            "information. Follow these guidelines:\n"
            "1. Include code examples when relevant to explain concepts\n"
            "2. Include measurements and numbers when relevant\n"
            "3. Keep explanations concise and direct\n"
            "4. Focus on facts, technical details and real-world usage\n"
            "5. Show basic and advanced usage patterns when relevant\n"
            "6. Use tables or lists to organize information when appropriate\n"
            "7. If show_citations is True, add numbered citations at the bottom in "
            "[1], [2] format"
        )

        messages = [{"role": "system", "content": system_message}]
        
        if context:
            messages.extend(context)
        
        messages.append({"role": "user", "content": query})
        
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream,
            "show_citations": show_citations
        }
        
        logging.debug(f"payload: {json.dumps(payload, indent=2)}")
        return payload

    def _handle_error(self, response: requests.Response) -> None:
        """Handle API error responses with specific exceptions."""
        error_msg = f"API request failed with status code {response.status_code}"
        
        if response.status_code == 401:
            raise AuthenticationError("Authentication failed. Please check your API key.")
        elif response.status_code == 429:
            raise APIError("Rate limit exceeded. Please wait before making more requests.")
        elif response.status_code == 500:
            raise APIError("Perplexity API server error. Please try again later.")
        
        try:
            error_details = response.json()
            error_msg += f": {error_details.get('error', {}).get('message', '')}"
        except:
            pass
        
        raise APIError(error_msg)

    def perform_search(self, query: str, model: str, stream: bool,
                      show_citations: bool, context: Optional[List[Dict[str, str]]] = None) -> Iterator[str]:
        logging.debug(f"Starting search with query: {query}, model: {model}, stream: {stream}, citations: {show_citations}")
        """Perform a search using the Perplexity API."""
        payload = self._build_payload(query, model, stream, show_citations, context)
        logging.debug(f"Payload: {payload}")

        response = requests.post(
            self.ENDPOINT,
            headers=self._get_headers(),
            json=payload,
            stream=stream  # Ensure this is set to the value of the `stream` parameter
        )
        logging.debug(f"Received response with status code: {response.status_code}")
        
        if response.status_code != 200:
            self._handle_error(response)

        if stream:
            logging.debug("Streaming response initiated.")
            yield from self._handle_stream_response(response, show_citations)
        else:
            try:
                response_data = response.json()
                logging.debug(f"Response  {response_data}")
                content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
                citations = response_data.get("citations", [])
                if citations and show_citations:
                    content += "\n\nReferences:\n" + "\n".join(f"[{i+1}] {url}" for i, url in enumerate(citations))
                yield content
            except json.JSONDecodeError:
                logging.error("Failed to decode JSON response.")
                yield ""


    def _parse_stream_line(self, line: bytes) -> Optional[Dict[str, Any]]:
        """Parse a single line from the stream."""
        if line:
            try:
                return json.loads(line.decode('utf-8').removeprefix('data: '))
            except json.JSONDecodeError:
                return None
        return None

    def _handle_stream_response(self, response: requests.Response, show_citations: bool) -> Iterator[str]:
        """Handle streaming response from Perplexity API."""
        accumulated_content = ""
        citations = []
        
        for line in response.iter_lines():
            data = self._parse_stream_line(line)
            if data:
                delta = data.get('choices', [{}])[0].get('delta', {})
                content = delta.get('content')
                if content:
                    accumulated_content += content
                    yield content  # Yield content as it arrives
                citations = data.get('citations', citations)
        
        if citations and show_citations:
            yield self._format_citations(citations)
        else:
            if not accumulated_content:
                logging.warning("No content received in streaming response.")

    def _format_citations(self, citations: List[str]) -> str:
        """Format citations into a string."""
        return "\n\nReferences:\n" + "\n".join(f"[{i+1}] {url}" for i, url in enumerate(citations))
