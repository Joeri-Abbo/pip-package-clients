# Clients

Clients is a Python package that provides client implementations for various backend services commonly used in
web applications. It includes clients for interacting with AWS DynamoDB, MySQL databases, and integrates with the Flask
web framework.

## Installation

You can install Clients using pip:

```bash
pip install Clients
``` 

Make sure to have the required dependencies listed in requirements.txt installed as well.

## Usage

### Flask Client

The FlaskClient class sets up a Flask application with CORS support and integrates with Sentry for error monitoring. You
can create an instance and configure the Flask app:

```python
from Clients.flask_client import FlaskClient

# Initialize the Flask app
flask_client = FlaskClient()
app = flask_client.get_client()

# Define your routes and application logic here
```

### SQL Client

The SQLClient class provides a client for MySQL databases. You can use it to execute SQL queries and fetch data:

```python
from Clients.sql_client import SQLClient

# Initialize the SQL client
sql_client = SQLClient()

# Execute a SQL query
query = "SELECT * FROM users WHERE username = %s"
params = ("john_doe",)
result = sql_client.fetch_one(query, params)
```

## Configuration

You can configure the clients by setting environment variables or using a .env file. Refer to the respective client
files for available configuration options.

## License

This project is licensed under the MIT License.