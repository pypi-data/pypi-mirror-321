from fastapi import FastAPI
from typing import List, Optional
import inspect
from pathlib import Path
from .router.router_manager import RouterManager
from .router.registry import ControllerRegistry
from .exceptions import register_exception_handlers
from .middleware import register_middlewares
import logging
import asyncio
import sys

logger = logging.getLogger(__name__)

class AppManager:
    """应用管理器"""
    _app: Optional[FastAPI] = None
    _initialized: bool = False
    _registered: bool = False

    @classmethod
    def init(
        cls,
        app: FastAPI,
        controllers_dir: Optional[str] = None,
        auto_scan: bool = True,
        cors_origins: Optional[List[str]] = None,
        cors_methods: Optional[List[str]] = None,
        cors_headers: Optional[List[str]] = None,
        cors_credentials: bool = True,
        cors_max_age: int = 600
    ) -> None:
        """
        初始化应用
        
        Args:
            app: FastAPI 应用实例
            controllers_dir: 控制器目录路径，如果提供则自动扫描
            auto_scan: 是否自动扫描控制器目录，默认为 True
            cors_*: CORS 配置参数
        """
        cls._app = app
        cls._initialized = True

        # 注册中间件
        register_middlewares(
            app,
            cors_origins=cors_origins,
            cors_methods=cors_methods,
            cors_headers=cors_headers,
            cors_credentials=cors_credentials,
            cors_max_age=cors_max_age
        )

        # 注册异常处理器
        register_exception_handlers(app)

        # 如果提供了控制器目录且启用了自动扫描，则扫描目录
        if controllers_dir and auto_scan:
            # 获取调用者的文件路径
            caller_frame = inspect.stack()[1]
            caller_file = Path(caller_frame.filename)
            base_dir = caller_file.parent

            # 如果是相对路径，则转换为绝对路径
            controllers_path = Path(controllers_dir)
            if not controllers_path.is_absolute():
                controllers_path = (base_dir / controllers_path).resolve()

            logger.debug(f"Scanning controllers directory: {controllers_path}")
            
            if controllers_path.exists():
                RouterManager.auto_include_routers(
                    app=app,
                    controllers_dir=str(controllers_path),
                    pattern="*_controller.py"
                )
            else:
                logger.warning(f"Controllers directory not found: {controllers_path}")

        # 注册当前模块中的路由器
        current_module = inspect.getmodule(inspect.stack()[1][0])
        if current_module:
            # 获取当前模块中定义的所有类
            for name, obj in inspect.getmembers(current_module):
                if inspect.isclass(obj) and hasattr(obj, '__module__') and obj.__module__ == current_module.__name__:
                    # 检查类是否有路由信息
                    if hasattr(obj, 'add_api_route'):
                        logger.debug(f"Found controller in current module: {name}")
                        router = obj()
                        app.include_router(router)

        # 等待所有装饰器执行完成后再注册其他路由器
        if asyncio.get_event_loop().is_running():
            asyncio.create_task(cls._delayed_register_routers())
        else:
            cls._register_routers()

        cls._registered = True

        # 打印所有注册的路由
        for route in app.routes:
            logger.debug(f"Registered route: {route.path} [{route.methods}]")

    @classmethod
    async def _delayed_register_routers(cls) -> None:
        """延迟注册路由器，确保所有装饰器都已执行"""
        await asyncio.sleep(0.1)
        cls._register_routers()

    @classmethod
    def get_app(cls) -> FastAPI:
        """获取应用实例"""
        if not cls._initialized:
            raise RuntimeError("Application not initialized. Call AppManager.init() first.")
        return cls._app

    @classmethod
    def _register_routers(cls) -> None:
        """注册所有装饰器注册的路由器（内部方法）"""
        if not cls._initialized:
            return
        
        # 获取所有注册的路由器
        routers = ControllerRegistry.get_routers()
        logger.debug(f"Found {len(routers)} routers in registry")
        
        # 获取已注册的路由路径集合
        existing_routes = {
            (route.path, frozenset(getattr(route, 'methods', set())))
            for route in cls._app.routes
        }
        
        # 包含所有装饰器注册的路由器
        for router in routers:
            # 检查路由器中的路由是否已存在
            router_routes = {
                (route.path, frozenset(route.methods))
                for route in router.routes
            }
            
            # 如果没有重复的路由（路径+方法组合）
            if not router_routes.intersection(existing_routes):
                logger.debug(f"Including router with prefix: {router.prefix}")
                logger.debug(f"Router routes: {router_routes}")
                cls._app.include_router(router)
                existing_routes.update(router_routes) 