# Flask Python Website

A simple Flask web application demonstrating route handling, template inheritance, and JSON responses.

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The server will start at `http://127.0.0.1:8000`

## Project Structure

```
FlaskPythonWebsiteFastasPossible/
├── static/
│   └── index.js         # Client-side JavaScript
├── templates/
│   ├── index.html       # Base template
│   └── profile.html     # Profile page template
├── app.py              # Main application file
├── views.py           # Route definitions
└── requirements.txt   # Project dependencies
```

## Available Routes

- `/views/` - Home page
- `/views/profile` - Profile page
- `/views/json` - Returns JSON data
- `/views/data` - Accepts and returns JSON data
- `/views/go-to-home` - Redirects to home page
- `/views/go-to-json` - Redirects to JSON endpoint
- `/views/nothome` - Simple text response

## Features

- Blueprint usage for route organization
- Template inheritance
- Static file serving
- JSON responses
- URL redirections
- Debug mode enabled

## Development

The application runs in debug mode by default on port 8000. You can modify these settings in `app.py`.
