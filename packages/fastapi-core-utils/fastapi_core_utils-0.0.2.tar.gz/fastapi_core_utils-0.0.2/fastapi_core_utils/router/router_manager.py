from typing import List, Union, Optional, Type
from pathlib import Path
import importlib.util
from fastapi import FastAPI, APIRouter
import logging
from types import ModuleType

logger = logging.getLogger(__name__)


class RouterManager:
    """路由管理器"""

    @staticmethod
    def _is_router(obj: Any) -> bool:
        """检查对象是否为 APIRouter 实例"""
        return isinstance(obj, APIRouter)

    @staticmethod
    def _load_module(file_path: Path) -> Optional[ModuleType]:
        """
        动态加载模块
        
        Args:
            file_path: 模块文件路径
            
        Returns:
            加载的模块对象，加载失败返回 None
        """
        try:
            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                logger.error(f"Failed to load module spec: {file_path}")
                return None
                
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            logger.error(f"Failed to load module {file_path}: {str(e)}")
            return None

    @classmethod
    def _find_routers_in_module(cls, module: ModuleType) -> List[APIRouter]:
        """
        在模块中查找所有路由器
        
        Args:
            module: 模块对象
            
        Returns:
            路由器列表
        """
        routers = []
        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
            attr = getattr(module, attr_name)
            if cls._is_router(attr):
                routers.append(attr)
        return routers

    @classmethod
    def auto_include_routers(
            cls,
            app: FastAPI,
            controllers_dir: Union[str, Path],
            pattern: str = "*_controller.py",
            prefix: str = "",
            tags: Optional[List[str]] = None
    ) -> None:
        """
        自动包含指定目录下的所有控制器

        Args:
            app: FastAPI 应用实例
            controllers_dir: 控制器目录路径
            pattern: 控制器文件匹配模式
            prefix: 路由前缀
            tags: API 标签列表
        """
        controllers_path = Path(controllers_dir)
        if not controllers_path.exists():
            logger.warning(f"Controllers directory not found: {controllers_dir}")
            return

        for controller_file in controllers_path.rglob(pattern):
            try:
                module = cls._load_module(controller_file)
                if module:
                    routers = cls._find_routers_in_module(module)
                    for router in routers:
                        app.include_router(
                            router, 
                            prefix=prefix if prefix else None,
                            tags=tags
                        )
                        logger.info(f"Loaded router from {controller_file.name}")
            except Exception as e:
                logger.error(f"Error loading controller {controller_file}: {str(e)}")

    @classmethod
    def include_routers(
        cls, 
        app: FastAPI, 
        routers: List[APIRouter],
        prefix: str = "",
        tags: Optional[List[str]] = None
    ) -> None:
        """
        手动包含路由器列表

        Args:
            app: FastAPI 应用实例
            routers: APIRouter 列表
            prefix: 路由前缀
            tags: API 标签列表
        """
        for router in routers:
            if cls._is_router(router):
                app.include_router(
                    router,
                    prefix=prefix if prefix else None,
                    tags=tags
                )
                logger.info(f"Included router: {router}")
            else:
                logger.warning(f"Invalid router object: {router}")
