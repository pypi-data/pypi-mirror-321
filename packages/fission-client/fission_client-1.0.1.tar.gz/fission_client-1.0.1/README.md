# Fission Python Client

This is an auto-generated Python client for the Fission API.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from fission_client import Configuration, ApiClient
from fission_client.api import FissionIoV1Api

# Configure API client
configuration = Configuration(host="YOUR_FISSION_SERVER_URL")
api_client = ApiClient(configuration)

# Create an instance of the API class
api_instance = FissionIoV1Api(api_client)

# Example: List functions
try:
    api_response = api_instance.list_fission_io_v1_function_for_all_namespaces()
    print(api_response)
except Exception as e:
    print("Exception when calling FissionIoV1Api: %s\n" % e)
```
