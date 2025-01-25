from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

def setup_cors(
    app: FastAPI,
    allow_origins: List[str] = ["*"],
    allow_methods: List[str] = ["*"],
    allow_headers: List[str] = ["*"],
    allow_credentials: bool = True,
    max_age: int = 600
) -> None:
    """
    设置 CORS 中间件
    
    Args:
        app: FastAPI 应用实例
        allow_origins: 允许的源列表，默认允许所有
        allow_methods: 允许的 HTTP 方法列表，默认允许所有
        allow_headers: 允许的 HTTP 头列表，默认允许所有
        allow_credentials: 是否允许携带凭证，默认允许
        max_age: 预检请求的最大缓存时间（秒），默认 600 秒
    """
    if "*" in allow_methods:
        allow_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
        
    if "*" in allow_headers:
        allow_headers = [
            "Accept",
            "Accept-Language",
            "Content-Language",
            "Content-Type",
            "Authorization",
            "X-Request-With",
            "X-Requested-With",
            "X-CSRF-Token",
        ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=allow_credentials,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
        max_age=max_age,
    ) 