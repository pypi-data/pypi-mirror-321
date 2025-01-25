from fastapi import FastAPI
from typing import List, Optional
from .response_handler import response_handler_middleware
from .cors_handler import setup_cors

def register_middlewares(
    app: FastAPI,
    cors_origins: Optional[List[str]] = None,
    cors_methods: Optional[List[str]] = None,
    cors_headers: Optional[List[str]] = None,
    cors_credentials: bool = True,
    cors_max_age: int = 600
) -> None:
    """
    注册所有中间件
    
    Args:
        app: FastAPI 应用实例
        cors_origins: CORS 允许的源列表，默认允许所有
        cors_methods: CORS 允许的方法列表，默认允许所有
        cors_headers: CORS 允许的头列表，默认允许所有
        cors_credentials: CORS 是否允许携带凭证，默认允许
        cors_max_age: CORS 预检请求的最大缓存时间（秒），默认 600 秒
    """
    # 设置 CORS
    setup_cors(
        app,
        allow_origins=cors_origins or ["*"],
        allow_methods=cors_methods or ["*"],
        allow_headers=cors_headers or ["*"],
        allow_credentials=cors_credentials,
        max_age=cors_max_age
    )
    
    # 注册响应处理中间件
    app.middleware("http")(response_handler_middleware) 