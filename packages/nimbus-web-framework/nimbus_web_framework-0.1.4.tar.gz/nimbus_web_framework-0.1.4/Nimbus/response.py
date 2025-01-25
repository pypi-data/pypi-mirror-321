from webob import Response as WebResponse
import json

class Response:
    def __init__(self):
        self.json = None
        self.html = None
        self.text = None
        self.content_type = None
        self.body = b''
        self.status_code = 200  # Default status code
        self.headers = {}  # Initialize headers as an empty dictionary

    def set_body_content_type(self):
        if self.json is not None:
            self.body = json.dumps(self.json).encode()
            self.content_type = "application/json"
            self.headers["Content-Type"] = self.content_type

        if self.html is not None:
            self.body = self.html.encode()
            self.content_type = "text/html"
            self.headers["Content-Type"] = self.content_type

        if self.text is not None:
            self.body = self.text.encode()  # Ensure text is encoded to bytes
            self.content_type = "text/plain"
            self.headers["Content-Type"] = self.content_type

    def __call__(self, environ, start_response):
        self.set_body_content_type()

        # Convert status_code to a proper status string (e.g., "200 OK")
        status = f"{self.status_code} OK"

        response = WebResponse(
            body=self.body,
            content_type=self.content_type,
            status=status  # Pass the status string here
        )

        return response(environ, start_response)