from typing import Any, Optional

class ArtCommException(Exception):
    """自定义业务异常基类"""
    
    def __init__(
        self,
        message: str,
        code: str = "1000",  # 修改为字符串类型
        data: Any = None,
        http_status_code: int = 200
    ):
        self.message = message
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        super().__init__(message)

class ValidationException(ArtCommException):
    """验证异常"""
    def __init__(self, message: str, data: Any = None):
        super().__init__(message, code="400", data=data)

class UnauthorizedException(ArtCommException):
    """未授权异常"""
    def __init__(self, message: str = "Unauthorized", data: Any = None):
        super().__init__(message, code="401", data=data)

class ForbiddenException(ArtCommException):
    """禁止访问异常"""
    def __init__(self, message: str = "Forbidden", data: Any = None):
        super().__init__(message, code="403", data=data)

class NotFoundException(ArtCommException):
    """资源不存在异常"""
    def __init__(self, message: str = "Resource not found", data: Any = None):
        super().__init__(message, code="404", data=data) 