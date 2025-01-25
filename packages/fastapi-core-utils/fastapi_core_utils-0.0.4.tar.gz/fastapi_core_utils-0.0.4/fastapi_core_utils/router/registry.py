from typing import List
from fastapi import APIRouter

class ControllerRegistry:
    """控制器注册表，用于收集所有被装饰的控制器"""
    _routers: List[APIRouter] = []

    @classmethod
    def register(cls, router: APIRouter) -> None:
        """注册路由器"""
        cls._routers.append(router)

    @classmethod
    def get_routers(cls) -> List[APIRouter]:
        """获取所有注册的路由器"""
        return cls._routers

    @classmethod
    def clear(cls) -> None:
        """清空注册表"""
        cls._routers.clear() 