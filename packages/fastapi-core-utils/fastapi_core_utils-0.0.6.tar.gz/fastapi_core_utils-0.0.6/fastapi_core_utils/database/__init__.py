"""
数据库管理模块

提供数据库连接、初始化和管理功能。

Example:
    ```python
    from fastapi import FastAPI
    from src.database import DBManager
    
    app = FastAPI()
    
    await DBManager.init_db(
        app=app,
        config="config/database.yaml",
        entity_dir="src/entity"
    )
    ```
"""

from .db_manager import DBManager

__all__ = [
    "DBManager",  # 数据库管理器
]