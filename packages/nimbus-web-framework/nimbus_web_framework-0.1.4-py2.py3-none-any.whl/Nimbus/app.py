from webob import Request
from parse import parse
import inspect
import requests
import wsgiadapter
from jinja2 import Environment, FileSystemLoader
import os
from whitenoise import WhiteNoise
from .middleware import Middleware
from .response import Response

class Nimbusapp:
    def __init__(self, templates_dir="templates", static_dir="static"):
        self.routes = {}

        # Jinja2 Template setup
        self.template_env = Environment(
            loader=FileSystemLoader(os.path.abspath(templates_dir))
        )
        self.exception_handler = None

        # WhiteNoise to serve static files
        self.static_dir = static_dir
        self.whitenoise = WhiteNoise(self.wsgi_app, root=static_dir, prefix="static")

        # Middleware setup
        self.middleware = Middleware(self)

    def __call__(self, environ, start_response):
        """Handle WSGI request and response cycle."""
        path_info = environ.get("PATH_INFO", "")

        # Handle static files
        if path_info.startswith("/static"):
            return self.whitenoise(environ, start_response)

        # Process through middleware and app
        return self.middleware(environ, start_response)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        start_response(f"{response.status_code} OK", list(response.headers.items()))
        return [response.body]

    def handle_request(self, request):
        """Handle the incoming request and return a response."""
        response = Response()

        handler_data, kwargs = self.find_handler(request)
        if handler_data is not None:
            handler = handler_data["handler"]
            allowed_methods = handler_data["allowed_methods"]

            # Handle class-based views
            if inspect.isclass(handler):
                handler_instance = handler()
                method = getattr(handler_instance, request.method.lower(), None)
                if method is None:
                    return self.method_not_allowed_response(response)

                method(request, response, **kwargs)
            else:
                # Function-based handlers
                if request.method.lower() not in allowed_methods:
                    return self.method_not_allowed_response(response)

                try:
                    handler(request, response, **kwargs)
                except Exception as e:
                    if self.exception_handler is not None:
                        self.exception_handler(request, response, e)
                    else:
                        raise e
        else:
            self.default_response(response)

        return response

    def find_handler(self, request):
        """Find the handler for the request."""
        for path, handler_data in self.routes.items():
            parsed_result = parse(path, request.path)
            if parsed_result is not None:
                return handler_data, parsed_result.named
        return None, None

    def default_response(self, response):
        """Default 404 response if no route is matched."""
        response.status_code = 404
        response.text = "Not Found"

    def method_not_allowed_response(self, response):
        """Return a 405 Method Not Allowed response."""
        response.status_code = 405
        response.text = "Method Not Allowed"
        return response

    def add_route(self, path, handler, allowed_methods=None):
        """Add a route to the app."""
        assert path not in self.routes, "Duplicate route. Please change the URL."

        if allowed_methods is None:
            allowed_methods = [
                "get",
                "post",
                "put",
                "head",
                "options",
                "delete",
                "patch",
                "connect",
                "trace",
            ]
        self.routes[path] = {"handler": handler, "allowed_methods": allowed_methods}

    def route(self, path, allowed_methods=None):
        """Route decorator for adding a route."""

        def wrapper(handler):
            self.add_route(path, handler, allowed_methods)
            return handler

        return wrapper

    def test_session(self):
        """Create a test session."""
        session = requests.Session()
        session.mount("https://testserver", wsgiadapter.WSGIAdapter(self))
        return session

    def template(self, template_name, context=None):
        """Render a Jinja2 template."""
        if context is None:
            context = {}
        return self.template_env.get_template(template_name).render(**context)

    def add_exception_handler(self, handler):
        """Add a global exception handler."""
        self.exception_handler = handler

    def add_middleware(self, middleware_cls):
        """Add middleware to the app."""
        self.middleware.add(middleware_cls)