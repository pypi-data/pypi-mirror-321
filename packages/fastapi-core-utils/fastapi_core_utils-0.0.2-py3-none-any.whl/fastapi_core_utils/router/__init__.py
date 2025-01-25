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

from .router_manager import RouterManager
from .decorators import controller, route

__version__ = "0.0.2"
__author__ = "刘浩"

__all__ = [
    "RouterManager",  # 路由管理器
    "controller",     # 控制器装饰器
    "route",         # 路由装饰器
]