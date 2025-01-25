from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from typing import Union
from .custom_exception import ArtCommException
from ..models.response import Response

async def artcomm_exception_handler(request: Request, exc: ArtCommException) -> JSONResponse:
    """处理自定义异常"""
    return JSONResponse(
        status_code=exc.http_status_code,
        content=Response(
            retCode=str(exc.code),
            retMsg=exc.message,
            retData=exc.data
        ).dict()
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """处理请求参数验证异常"""
    return JSONResponse(
        status_code=200,
        content=Response(
            retCode="400",
            retMsg="Invalid request parameters",
            retData=[{"loc": err["loc"], "msg": err["msg"]} for err in exc.errors()]
        ).dict()
    )

async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """处理HTTP异常"""
    return JSONResponse(
        status_code=200,
        content=Response(
            retCode=str(exc.status_code),
            retMsg=str(exc.detail)
        ).dict()
    )

async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """处理其他所有异常"""
    return JSONResponse(
        status_code=200,
        content=Response(
            retCode="500",
            retMsg=f"Internal server error: {str(exc)}"
        ).dict()
    ) 