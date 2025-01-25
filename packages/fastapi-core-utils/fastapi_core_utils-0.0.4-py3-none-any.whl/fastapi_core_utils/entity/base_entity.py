from tortoise.models import Model
from tortoise import fields
from typing import Any, Dict, Optional
import datetime


class BaseEntity(Model):
    """基础实体类"""
    
    id = fields.IntField(pk=True, description="主键ID")
    create_time = fields.DatetimeField(
        auto_now_add=True, 
        index=True,
        description="创建时间"
    )
    update_time = fields.DatetimeField(
        auto_now=True,
        description="更新时间"
    )

    class Meta:
        abstract = True

    @staticmethod
    def _to_camel_case(snake_str: str) -> str:
        """将下划线命名转换为小驼峰命名"""
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典（字段名自动转换为小驼峰）"""
        data = {}
        # 获取所有字段
        for field_name, field in self._meta.fields_map.items():
            value = getattr(self, field_name)
            # 处理日期时间类型
            if isinstance(value, (datetime.date, datetime.datetime)):
                value = value.isoformat()
            # 处理枚举类型
            elif hasattr(value, 'value'):
                value = value.value
            # 转换字段名为小驼峰
            camel_name = self._to_camel_case(field_name)
            data[camel_name] = value
        return data

    @classmethod
    async def get_by_id(cls, id: int) -> Optional['BaseEntity']:
        """根据ID查询"""
        return await cls.get_or_none(id=id)
