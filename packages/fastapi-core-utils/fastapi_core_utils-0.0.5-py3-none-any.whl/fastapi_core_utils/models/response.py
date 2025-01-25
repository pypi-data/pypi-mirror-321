from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    """统一响应模型"""
    retCode: str = "0000"  # 修改为字符串类型
    retMsg: str = "success"
    retData: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            # 添加自定义序列化器
        }

    @classmethod
    def success(cls, data: Any = None, message: str = "success") -> 'Response':
        """成功响应"""
        return cls(retCode="0000", retMsg=message, retData=data)

    @classmethod
    def error(cls, code: str = "1000", message: str = "error", data: Any = None) -> 'Response':
        """错误响应"""
        return cls(retCode=code, retMsg=message, retData=data) 