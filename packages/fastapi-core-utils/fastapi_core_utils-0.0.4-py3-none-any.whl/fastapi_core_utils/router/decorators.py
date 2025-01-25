from functools import wraps
from typing import List, Optional, Any, Callable
from fastapi import APIRouter, Response
import inspect
from .registry import ControllerRegistry
import logging

logger = logging.getLogger(__name__)

class RouteDecorator:
    """路由装饰器类"""
    
    def __init__(self, path: str = None, **kwargs):
        self.path = path
        self.kwargs = kwargs
    
    def __call__(self, func: Callable) -> Callable:
        if self.path is None:
            return func
        func._path = self.path
        func._methods = self.kwargs.pop('methods', ['GET'])
        func._kwargs = self.kwargs
        return func
    
    def get(self, path: str, **kwargs) -> Callable:
        """GET 请求装饰器"""
        kwargs['methods'] = ['GET']
        return RouteDecorator(path, **kwargs)
    
    def post(self, path: str, **kwargs) -> Callable:
        """POST 请求装饰器"""
        kwargs['methods'] = ['POST']
        return RouteDecorator(path, **kwargs)
    
    def put(self, path: str, **kwargs) -> Callable:
        """PUT 请求装饰器"""
        kwargs['methods'] = ['PUT']
        return RouteDecorator(path, **kwargs)
    
    def delete(self, path: str, **kwargs) -> Callable:
        """DELETE 请求装饰器"""
        kwargs['methods'] = ['DELETE']
        return RouteDecorator(path, **kwargs)


# 创建全局路由装饰器实例
route = RouteDecorator()


def controller(
    prefix: str = "", 
    tags: Optional[List[str]] = None,
    responses: dict = None,
    **kwargs
):
    """
    控制器装饰器，用于创建路由器
    """
    def decorator(cls):
        logger.debug(f"Decorating class {cls.__name__} with controller")
        
        # 创建路由器
        router = APIRouter(
            prefix=prefix, 
            tags=tags,
            responses=responses,
            **kwargs
        )

        # 创建类实例
        instance = cls()

        # 获取类中所有方法
        for attr_name, attr in inspect.getmembers(cls, inspect.isfunction):
            if hasattr(attr, "_path"):
                # 获取路由信息
                path = getattr(attr, "_path")
                methods = getattr(attr, "_methods", ["GET"])
                route_kwargs = getattr(attr, "_kwargs", {})

                # 合并响应定义
                if responses:
                    route_kwargs['responses'] = {
                        **responses,
                        **(route_kwargs.get('responses', {}))
                    }

                # 获取绑定方法
                endpoint = getattr(instance, attr_name)
                
                logger.debug(f"Adding route {methods} {path} to router")
                
                # 注册路由
                router.add_api_route(
                    path=path,
                    endpoint=endpoint,
                    methods=methods,
                    **route_kwargs
                )

        # 注册到注册表
        logger.debug(f"Registering router with prefix {prefix} to registry")
        ControllerRegistry.register(router)
        
        # 返回原始类，而不是路由器
        return cls

    return decorator


def route(
    path: str, 
    methods: Optional[List[str]] = None, 
    response_model: Any = None,
    **kwargs
) -> Callable:
    """
    路由装饰器，用于标记控制器方法

    Args:
        path: 路由路径
        methods: HTTP 方法列表
        response_model: 响应模型
        **kwargs: 其他 FastAPI 路由参数
    """
    def decorator(func: Callable) -> Callable:
        func._path = path
        func._methods = methods or ["GET"]
        if response_model:
            kwargs['response_model'] = response_model
        func._kwargs = kwargs
        return func
    return decorator


# 为常用 HTTP 方法提供快捷装饰器
def get(path: str, **kwargs) -> Callable:
    """GET 请求装饰器"""
    return route(path, methods=["GET"], **kwargs)

def post(path: str, **kwargs) -> Callable:
    """POST 请求装饰器"""
    return route(path, methods=["POST"], **kwargs)

def put(path: str, **kwargs) -> Callable:
    """PUT 请求装饰器"""
    return route(path, methods=["PUT"], **kwargs)

def delete(path: str, **kwargs) -> Callable:
    """DELETE 请求装饰器"""
    return route(path, methods=["DELETE"], **kwargs)
