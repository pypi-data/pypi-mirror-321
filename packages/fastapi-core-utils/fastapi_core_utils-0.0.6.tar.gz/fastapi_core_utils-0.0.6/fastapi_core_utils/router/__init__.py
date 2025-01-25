"""
路由管理模块

提供路由注册和控制器管理功能。

Example:
    ```python
    from fastapi import FastAPI
    from src.router import RouterManager, controller, route
    
    app = FastAPI()
    
    @controller(prefix="/api", tags=["示例"])
    class ExampleController:
        @route.get("/hello", summary="示例接口")
        async def hello(self):
            return {"message": "Hello World"}
    ```
"""

from .decorators import controller, get, post, put, delete, route
from .router_manager import RouterManager
from .registry import ControllerRegistry
from .base_controller import BaseController


__all__ = [
    'controller',
    'get', 'post', 'put', 'delete', 'route',
    'RouterManager',
    'ControllerRegistry',
    'BaseController'
]