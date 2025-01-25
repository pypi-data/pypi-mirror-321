# 路由管理模块

提供路由注册和控制器管理功能，支持装饰器风格的路由定义。

## 基础用法

```python
from fastapi import FastAPI
from fastapi_core_utils.router import RouterManager, controller, route
from typing import Dict, List

app = FastAPI()


@controller(prefix="/api/v1", tags=["用户管理"])
class UserController:
   @route.get("/users", response_model=List[UserSchema], summary="获取用户列表")
   async def get_users(self):
      return await UserService.get_users()

   @route.post("/users", response_model=UserSchema, summary="创建用户")
   async def create_user(self, user: UserCreateSchema):
      return await UserService.create_user(user)

   @route.get(
      "/users/{user_id}",
      summary="获取用户详情",
      responses={404: {"description": "用户不存在"}}
   )
   async def get_user(self, user_id: int):
      return await UserService.get_user(user_id)


# 方式1：自动扫描加载控制器
RouterManager.auto_include_routers(
   app=app,
   controllers_dir="src/controllers",
   pattern="*_controller.py"
)

# 方式2：手动加载控制器
RouterManager.include_routers(
   app=app,
   routers=[UserController]
)
```

## 特性

1. 装饰器支持
   - `@controller`: 控制器装饰器
   - `@route.get`: GET 请求装饰器
   - `@route.post`: POST 请求装饰器
   - `@route.put`: PUT 请求装饰器
   - `@route.delete`: DELETE 请求装饰器
   - `@route`: 通用路由装饰器

2. 路由管理
   - 支持自动扫描控制器文件
   - 支持递归扫描子目录
   - 支持手动注册路由器
   - 支持全局路由前缀和标签

3. 响应处理
   - 支持响应模型定义
   - 支持公共响应配置
   - 自动处理 Response 对象

## 最佳实践

1. 控制器组织
   - 按功能模块组织控制器
   - 文件名以 `_controller.py` 结尾
   - 类名以 `Controller` 结尾

2. 路由定义
   - 使用语义化的路径
   - 合理使用 HTTP 方法
   - 添加适当的标签和描述

3. 响应处理
   - 使用响应模型规范返回格式
   - 定义公共错误响应
   - 添加适当的状态码

4. 目录结构示例
```
src/
  controllers/
    user/
      user_controller.py
      auth_controller.py
    product/
      product_controller.py
      category_controller.py
```

## 注意事项

1. 控制器文件命名必须符合匹配模式（默认 `*_controller.py`）
2. 控制器类必须使用 `@controller` 装饰器
3. 路由方法必须使用路由装饰器（`@route.get`、`@route.post` 等）
4. 建议为每个控制器指定合适的标签和前缀
```


```python

from fastapi_core_utils.router import controller, route

@controller(prefix="/api", tags=["示例"])
class ExampleController:
    @route("/hello", methods=["GET"])
    async def hello(self):
        return {"message": "Hello World"}
```