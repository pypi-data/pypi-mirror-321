# linnworks-api-python

This is a python version of the Linnworks API
<https://apidocs.linnworks.net/reference/overview>

We use the openapi generator <https://openapi-generator.tech/> to convert the linnworks api
swagger api models <https://github.com/LinnSystems/PublicApiSpecs> into a python package.

This creates a `requests` based API with `pydantic` types. Awesome!

This project consists of tweaks I had to make to aws auth schemes to get things working
with the openapi generator client, the generator script that creates the models and a
little bit of documentation. Nothing fancy.

## Prerequisites

- python 3.9+
- linnworks api credentials. See the docs <https://apidocs.linnworks.net/reference/setting-up>

## Installation

`pip install linnworks-api-python`

## Usage

```python
import os
from linnworks_api.generated.auth.api import AuthApi
from linnworks_api.generated.auth.models.authorize_by_application_request import AuthorizeByApplicationRequest

from linnworks_api.generated.inventory.api import InventoryApi
from linnworks_api.generated.inventory.base_client import LinnworksConfig, LinnworksClient as InventoryClient

# Mock responses
from dotenv import load_dotenv

load_dotenv()


def test_auth():
    """This is an example of how to get an auth token"""
    props = AuthorizeByApplicationRequest(
        ApplicationId=os.getenv("LW_CLIENT_ID"),
        ApplicationSecret=os.getenv("LW_CLIENT_SECRET"),
        Token=os.getenv("LW_TOKEN"),
    )
    auth_api = AuthApi()
    response = auth_api.authorize_by_application(props)
    assert isinstance(response.token, str)


def test_inventory():
    """This is an example of how to create a client and make an API call"""
    inventory_client = InventoryClient(
        linnworks_config=LinnworksConfig(
            client_id=os.getenv("LW_CLIENT_ID"),
            client_secret=os.getenv("LW_CLIENT_SECRET"),
            token=os.getenv("LW_TOKEN"),
        )
    )
    inventory_api = InventoryApi(inventory_client)
    response = inventory_api.get_inventory_items_count()
    assert response == 1
```

## Development

This is a poetry project so do the normal `poetry install` type things to set up your environment. 

We use a Makefile for build automation.

- `make clean` removes the generated code
- `make generate` generates the schemas
- `make test` runs unit tests
- `make lint-fix` fixes linting issues and checks compliance with linting standards

### Project Structure

```text
.
├── Makefile - make scripts
├── README.md - this file
├── notebooks
│   └── api_test.ipynb - example usage
├── poetry.lock
├── pyproject.toml
├── PublicApiSpecs - the linnworks swagger models. A git submodule
├── scripts
│   └── generate_schemas.py - script to generate api
├── tests - unit tests. (just enough to make sure things generated without error)
└── src
    └── linnworks_api
        |── base_client.py - client that gets copied into each package in generated/
        └── generated - the generated api files created when generate_schemas.py is run
```
