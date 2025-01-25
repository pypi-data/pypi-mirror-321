# 实体模块

## 基础实体类

所有业务实体都应继承自 `BaseEntity`，它提供了以下功能：

### 基础字段
- `id`: 主键ID (IntField)
- `create_time`: 创建时间 (DatetimeField)
- `update_time`: 更新时间 (DatetimeField)

### 内置方法
- `to_dict()`: 将实体转换为字典（自动转换为小驼峰命名）
- `get_by_id()`: 根据ID查询
- `update_fields()`: 更新指定字段

## 使用示例

```python
from tortoise import fields
from fastapi_core_utils.entity.base_entity import BaseEntity


class User(BaseEntity):
   """用户实体"""

   username = fields.CharField(
      max_length=50,
      unique=True,
      description="用户名"
   )
   email_address = fields.CharField(
      max_length=100,
      unique=True,
      description="邮箱地址"
   )
   phone_number = fields.CharField(
      max_length=20,
      null=True,
      description="手机号码"
   )
   status = fields.IntEnumField(
      UserStatus,  # 假设有个 UserStatus 枚举
      default=UserStatus.ACTIVE,
      description="用户状态"
   )

   class Meta:
      table = "users"
      table_description = "用户信息表"

   def to_dict(self) -> Dict[str, Any]:
      # 继承父类的 to_dict 方法，添加自己的字段
      base_dict = super().to_dict()
      return {
         **base_dict,
         'username': self.username,
         'emailAddress': self.email_address,
         'phoneNumber': self.phone_number,
         'status': self.status.value
      }


# 使用示例
async def example():
   # 创建用户
   user = await User.create(
      username="test_user",
      email_address="test@example.com",
      phone_number="1234567890"
   )

   # 查询用户
   user = await User.get_by_id(1)

   # 更新字段
   await user.update_fields(
      phone_number="9876543210",
      remark="Updated phone number"
   )

   # 转换为字典（自动转换为小驼峰命名）
   user_dict = user.to_dict()
```

## 最佳实践

1. 字段定义
   - 使用合适的字段类型
   - 添加合适的约束（长度、唯一性等）
   - 提供字段描述
   - 考虑是否需要索引

2. 表配置
   - 指定表名
   - 添加表描述
   - 配置合适的索引

3. 方法扩展
   - 根据业务需求扩展基础实体类的方法
   - 重写 to_dict 方法时记得调用父类方法

4. 字段命名
   - 使用下划线命名（snake_case）
   - `to_dict()` 方法会自动转换为小驼峰命名（camelCase）
   - 例如：`email_address` -> `emailAddress`

5. 特殊类型处理
   - 日期时间类型会自动转换为 ISO 格式字符串
   - 枚举类型会自动获取其值

6. 命名规范
   - 实体文件以 `_entity.py` 结尾
   - 类名使用大驼峰命名（PascalCase）
   - 字段名使用下划线命名（snake_case）