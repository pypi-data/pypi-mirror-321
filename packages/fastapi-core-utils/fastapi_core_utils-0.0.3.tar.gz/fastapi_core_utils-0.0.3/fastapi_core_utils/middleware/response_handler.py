from fastapi import Request, Response as FastAPIResponse
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse, StreamingResponse
from ..models.response import Response
import json

# 不需要包装的路径
SKIP_PATHS = {
    "/docs",
    "/redoc",
    "/openapi.json",
    "/docs/oauth2-redirect",
    "/favicon.ico"
}

# 不需要包装的响应类型
SKIP_RESPONSE_TYPES = (
    HTMLResponse,
    RedirectResponse,
    StreamingResponse
)

async def response_handler_middleware(request: Request, call_next):
    """响应处理中间件，统一响应格式"""
    # 跳过特定路径
    if request.url.path in SKIP_PATHS:
        return await call_next(request)

    response = await call_next(request)
    
    # 跳过特定响应类型
    if isinstance(response, SKIP_RESPONSE_TYPES):
        return response

    # 如果响应是 Response 对象，直接返回
    if isinstance(response, Response):
        return JSONResponse(
            status_code=200,
            content=response.dict()
        )
    
    # 如果是 FastAPI Response 对象，尝试获取内容
    if isinstance(response, FastAPIResponse):
        try:
            body = await response.body()
            if body:
                content = json.loads(body)
                # 如果已经是标准格式，直接返回
                if isinstance(content, dict) and all(key in content for key in ['retCode', 'retMsg', 'retData']):
                    return JSONResponse(
                        status_code=200,
                        content=content
                    )
                # 否则包装为标准格式
                return JSONResponse(
                    status_code=200,
                    content=Response(
                        retCode="0000",
                        retMsg="success",
                        retData=content
                    ).dict()
                )
        except:
            # 如果无法解析为 JSON，返回原始响应
            return response
    
    # 如果是其他类型的响应，尝试包装
    try:
        return JSONResponse(
            status_code=200,
            content=Response(
                retCode="0000",
                retMsg="success",
                retData=response
            ).dict()
        )
    except:
        # 如果无法序列化，返回原始响应
        return response 