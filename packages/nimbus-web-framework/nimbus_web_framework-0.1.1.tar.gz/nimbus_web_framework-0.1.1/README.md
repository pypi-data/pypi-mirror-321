

# Nimbus Web Framework

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-0.1.0-orange)
![PyPI](https://img.shields.io/pypi/v/nimbus-web-framework)


**Nimbus** is a lightweight Python web framework designed for simplicity and performance. Built for learning purposes, it provides essential features like routing, middleware support, template rendering, and static file serving.

---

## Features

- **Easy Routing**: Define routes with support for dynamic URL parameters.
- **Middleware Support**: Add custom middleware for request/response processing.
- **Template Rendering**: Use Jinja2 templates for dynamic HTML content.
- **Static File Serving**: Serve static files (CSS, JS, images) with WhiteNoise.
- **JSON Responses**: Easily return JSON data from your routes.
- **Exception Handling**: Custom exception handlers for better error management.



---

## Installation

Install **Nimbus Web Framework** via pip:

```shell
pip install nimbus-web-framework
```

---

## Quick Start

### 1. Create a Simple App

```python
from nimbus import Nimbusapp

app = Nimbusapp()

@app.route("/")
def home(request, response):
    response.text = "Hello, World!"

if __name__ == "__main__":
    app.run()
```

### 2. Run the App

Start the development server:

```bash
python app.py
```

Visit `http://localhost:8080` in your browser to see "Hello, World!".

---

## Basic Usage

### Routing

Define routes with the `@app.route` decorator:

```python
@app.route("/about")
def about(request, response):
    response.text = "About Us"
```

### Dynamic Routes

Capture URL parameters:

```python
@app.route("/hello/{name}")
def greet(request, response, name):
    response.text = f"Hello, {name}!"
```

### Template Rendering

Use Jinja2 templates to render HTML:

```python
@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "test.html",
        context={"title": "Nimbus", "message": "Welcome to Nimbus!"}
    )
```

### Static Files

Serve static files (CSS, JS, images) from the `static/` directory:

```html
<link rel="stylesheet" href="/static/test.css">
```

### JSON Responses

Return JSON data:

```python
@app.route("/json")
def json_handler(request, response):
    response.json = {"status": "success", "message": "Hello, JSON!"}
```

### Middleware

Add custom middleware:

```python
class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def process_request(self, req):
        print(f"Request: {req.url}")

    def process_response(self, req, resp):
        print(f"Response: {resp.status_code}")

app.add_middleware(LoggingMiddleware)
```



## Testing

The framework includes a comprehensive test suite to ensure functionality. To run the tests:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nimbus-web-framework.git
   cd nimbus-web-framework
   ```

2. Install the development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest tests/test_app.py
   ```

### Example Test File (`test_app.py`)

The `test_app.py` file includes tests for the following features:

#### 1. **Basic Routing**
   - Tests if a simple route returns the correct response.
   ```python
   def test_basic_route_adding(app, test_client):
       @app.route("/home")
       def home(req, resp):
           resp.text = "Hello from home"

       response = test_client.get("https://testserver/home")
       assert response.text == "Hello from home"
   ```

#### 2. **Dynamic Routes**
   - Tests if dynamic routes with URL parameters work correctly.
   ```python
   def test_dynamic_route(app, test_client):
       @app.route("/hello/{name}")
       def greet(req, resp, name):
           resp.text = f"Hello, {name}!"

       response = test_client.get("https://testserver/hello/Abulqosim")
       assert response.text == "Hello, Abulqosim!"
   ```

#### 3. **Template Rendering**
   - Tests if templates are rendered correctly with context variables.
   ```python
   def test_template_handler(app, test_client):
       @app.route("/template")
       def template(req, resp):
           resp.html = app.template(
               "test.html",
               context={"title": "Nimbus", "message": "Welcome to Nimbus!"}
           )
       response = test_client.get("https://testserver/template")
       assert "Welcome to Nimbus!" in response.text
   ```

#### 4. **Static Files**
   - Tests if static files are served correctly.
   ```python
   def test_static_file_serving(test_client):
       response = test_client.get("https://testserver/static/styles.css")
       assert response.status_code == 200
       assert "text/css" in response.headers["Content-Type"]
   ```

#### 5. **JSON Responses**
   - Tests if JSON responses are returned correctly.
   ```python
   def test_json_response(app, test_client):
       @app.route("/json")
       def json_handler(req, resp):
           resp.json = {"status": "success", "message": "Hello, JSON!"}

       response = test_client.get("https://testserver/json")
       assert response.json() == {"status": "success", "message": "Hello, JSON!"}
   ```

#### 6. **Middleware**
   - Tests if middleware processes requests and responses correctly.
   ```python
   def test_middleware(app, test_client):
       class LoggingMiddleware:
           def __init__(self, app):
               self.app = app

           def process_request(self, req):
               print(f"Request: {req.url}")

           def process_response(self, req, resp):
               print(f"Response: {resp.status_code}")

       app.add_middleware(LoggingMiddleware)

       @app.route("/middleware")
       def middleware_test(req, resp):
           resp.text = "Middleware test"

       response = test_client.get("https://testserver/middleware")
       assert response.text == "Middleware test"
   ```

---



Got it! If you want to include information about **template rendering** in the `README.md`, here’s how you can add a section specifically for templates:

---

## Template Rendering

Nimbus Web Framework supports **Jinja2 templates** for rendering dynamic HTML content. You can easily render templates and pass context variables to them.

### Example: Rendering a Template

1. Create a template file (e.g., `test.html`) in the `templates/` directory:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{{ title }}</title>
   </head>
   <body>
       <h1>{{ title }}</h1>
       <p>{{ message }}</p>
   </body>
   </html>
   ```

2. Use the `app.template` method to render the template in your route:
   ```python
   @app.route("/template")
   def template_handler(request, response):
       response.html = app.template(
           "test.html",
           context={"title": "Nimbus", "message": "Welcome to Nimbus!"}
       )
   ```

3. When you visit `http://localhost:8080/template`, the rendered HTML will look like this:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Nimbus</title>
   </head>
   <body>
       <h1>Nimbus</h1>
       <p>Welcome to Nimbus!</p>
   </body>
   </html>
   ```






Got it! Here's how you can add a **Static Files** section to your `README.md` to explain how static files (CSS, JS, images, etc.) are handled in your framework:

---

## Static Files

Nimbus Web Framework uses **WhiteNoise** to serve static files like CSS, JavaScript, and images. Static files are served from the `static/` directory.

### Example: Serving Static Files

1. Create a `static/` directory in your project root and add your static files. For example:
   ```
   static/
   ├── styles.css
   ├── script.js
   └── images/
       └── logo.png
   ```

2. Link to the static files in your HTML templates or responses:
   ```html
   <link rel="stylesheet" href="/static/styles.css">
   <script src="/static/script.js"></script>
   <img src="/static/images/logo.png" alt="Logo">
   ```

3. When you run your app, static files will be automatically served from the `static/` directory.

### Example: Serving a CSS File

1. Add a CSS file (`styles.css`) to the `static/` directory:
   ```css
   body {
       background-color: lightblue;
       font-family: Arial, sans-serif;
   }
   ```

2. Link to the CSS file in your HTML template:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <link rel="stylesheet" href="/static/test.css">
       <title>Static Files Example</title>
   </head>
   <body>
       <h1>Welcome to Nimbus!</h1>
       <p>This page uses a static CSS file.</p>
   </body>
   </html>
   ```

3. When you visit the page, the CSS will be applied.

### Testing Static File Serving

You can test static file serving using the following test:

```python
def test_static_file_serving(test_client):
    response = test_client.get("https://testserver/static/styles.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["Content-Type"]
    assert "background-color" in response.text
```

---
