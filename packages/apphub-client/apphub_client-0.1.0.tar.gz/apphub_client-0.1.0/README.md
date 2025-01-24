# Fission Python Client

This is an auto-generated Python client for the Fission API.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from apphub_client import Configuration, ApiClient
from apphub_client.api import ApphubV1Api

# Configure API client
configuration = Configuration(host="YOUR_FISSION_SERVER_URL")
api_client = ApiClient(configuration)

# Create an instance of the API class
api_instance = ApphubV1Api(api_client)

# Example: List functions
try:
    api_response = api_instance.list_apphub_v1_function_for_all_namespaces()
    print(api_response)
except Exception as e:
    print("Exception when calling ApphubV1Api: %s\n" % e)
```
