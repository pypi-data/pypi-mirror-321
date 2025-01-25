from tortoise.contrib.fastapi import RegisterTortoise
from typing import Dict, List, Optional, Union
from pathlib import Path
import importlib.util
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import yaml
import json
import logging
from datetime import datetime
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

logger = logging.getLogger(__name__)


class DBConfig:
    """数据库配置类"""
    def __init__(self, config: Dict):
        self.db_conf = config.get('mysql', config.get('database', {}))
        self._validate_config()
        
    def _validate_config(self):
        required_fields = ['host', 'port', 'database']
        if 'db_url' not in self.db_conf:
            required_fields.extend(['username', 'password'])
            
        missing_fields = [field for field in required_fields 
                         if field not in self.db_conf]
        if missing_fields:
            raise ValueError(f"Missing required database config: {missing_fields}")
            
    @property
    def db_url(self) -> str:
        if 'db_url' in self.db_conf:
            return self.db_conf['db_url']
            
        return (f'mysql://{self.db_conf["username"]}:{self.db_conf["password"]}'
                f'@{self.db_conf["host"]}:{self.db_conf["port"]}/{self.db_conf["database"]}')


class DBManager:
    """数据库管理器"""

    @staticmethod
    def _load_config(config_path: Union[str, Path, Dict]) -> Dict:
        """
        加载数据库配置
        支持 yaml、json 文件或直接传入字典
        """
        if isinstance(config_path, dict):
            return config_path

        config_path = Path(config_path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, 'r', encoding='utf-8') as f:
            if config_path.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif config_path.suffix == '.json':
                return json.load(f)
            else:
                raise ValueError(f"Unsupported config file format: {config_path.suffix}")

    @staticmethod
    def _get_db_url(config: Dict) -> str:
        """构建数据库连接 URL"""
        db_config = DBConfig(config)
        return db_config.db_url

    @classmethod
    def _find_entity_modules(cls, entity_dir: Union[str, Path]) -> List[str]:
        """扫描实体目录，返回所有实体模块路径"""
        entity_path = Path(entity_dir)
        if not entity_path.exists():
            logger.warning(f"Entity directory not found: {entity_dir}")
            return []

        modules = []
        for file in entity_path.rglob("*_entity.py"):
            # 将文件路径转换为模块路径
            relative_path = file.relative_to(entity_path.parent)
            module_path = str(relative_path).replace('/', '.').replace('\\', '.')[:-3]
            modules.append(module_path)

        return modules

    @classmethod
    async def init_db(
            cls,
            app: FastAPI,
            config: Union[str, Path, Dict],
            entity_dir: Optional[Union[str, Path]] = None,
            modules: Optional[List[str]] = None,
            generate_schemas: bool = True,
            add_exception_handlers: bool = True
    ) -> None:
        """
        初始化数据库

        Args:
            app: FastAPI 应用实例
            config: 配置文件路径或配置字典
            entity_dir: 实体目录路径（用于自动扫描）
            modules: 实体模块列表（手动指定）
            generate_schemas: 是否自动生成表结构
            add_exception_handlers: 是否添加异常处理器
        """
        # 加载配置
        db_config = cls._load_config(config)

        # 获取数据库连接 URL
        db_url = cls._get_db_url(db_config)

        # 获取实体模块列表
        entity_modules = []
        if entity_dir:
            entity_modules.extend(cls._find_entity_modules(entity_dir))
        if modules:
            entity_modules.extend(modules)

        if not entity_modules:
            raise ValueError("No entity modules found or specified")

        # 获取时区设置
        timezone_config = db_config.get('timezone', {})
        use_tz = timezone_config.get('use_tz', False)
        timezone = timezone_config.get('timezone', 'Asia/Shanghai')

        # 获取连接池配置
        pool_config = db_config.get('pool', {})
        connection_params = {
            'max_size': pool_config.get('max_size', 10),
            'min_size': pool_config.get('min_size', 1),
            'max_inactive_connection_lifetime': 
                pool_config.get('max_inactive_connection_lifetime', 300)
        }

        # 初始化数据库
        await RegisterTortoise(
            app=app,
            db_url=db_url,
            modules={"models": entity_modules},
            generate_schemas=generate_schemas,
            add_exception_handlers=add_exception_handlers,
            use_tz=use_tz,
            timezone=timezone,
            **connection_params  # 添加连接池配置
        )

        logger.info(f"Database initialized with {len(entity_modules)} entity modules")

    @staticmethod
    async def health_check() -> bool:
        """数据库健康检查"""
        try:
            conn = Tortoise.get_connection("default")
            await conn.execute_query("SELECT 1")
            return True
        except DBConnectionError:
            return False
