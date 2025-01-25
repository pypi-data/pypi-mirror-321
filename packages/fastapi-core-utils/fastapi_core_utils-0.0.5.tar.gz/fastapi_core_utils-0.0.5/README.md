# FastAPI Utils

FastAPI utilities for rapid development.

## Features

- Database Management
  - Easy database initialization
  - Entity base class with common fields
  - YAML/JSON configuration support

- Router Management
  - Decorator-based routing
  - Auto-scanning controllers
  - Easy route grouping

## Installation

```bash
pip install fastapi-core-utils
```

## Quick Start

```python
from fastapi import FastAPI
from fastapi_core_utils.router import RouterManager, controller, route
from fastapi_core_utils.database import DBManager

app = FastAPI()

# Initialize database
await DBManager.init_db(
  app=app,
  config="config/database.yaml",
  entity_dir="fastapi_core_utils/entity"
)


# Define controller
@controller(prefix="/api", tags=["example"])
class ExampleController:
  @route.get("/hello")
  async def hello(self):
    return {"message": "Hello World"}


# Auto include controllers
RouterManager.auto_include_routers(
  app=app,
  controllers_dir="app/src/controllers"
)
```

## Documentation

For more details, please visit our [GitHub repository](https://github.com/yourusername/fastapi-core-utils).

## License

This project is licensed under the MIT License. 



```shell
rm -rf dist/ build/ *.egg-info/
```
```shell
python -m build
```
```shell
python -m twine upload dist/*
```