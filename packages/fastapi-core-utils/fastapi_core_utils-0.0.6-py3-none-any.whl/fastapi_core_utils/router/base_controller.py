from typing import Any, Dict, Optional
from ..models.response import Response

class BaseController:
    """基础控制器类，提供统一的响应方法"""
    
    def ok(self, data: Any = None, msg: str = "success"):
        """成功响应"""
        return Response.success(data=data, message=msg)
    
    def fail(self, msg: str = "error", code: int = 500, data: Any = None):
        """失败响应"""
        return Response.error(message=msg, data=data)