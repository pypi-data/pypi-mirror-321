from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from .handlers import (
    artcomm_exception_handler,
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler
)
from .custom_exception import (
    ArtCommException,
    ValidationException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException
)

def register_exception_handlers(app: FastAPI) -> None:
    """注册所有异常处理器"""
    app.add_exception_handler(ArtCommException, artcomm_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler) 