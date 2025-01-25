# 数据库管理模块

## 配置示例

```yaml
# 方式1：详细配置
mysql:
  host: localhost
  port: 3306
  database: your_database
  username: your_username
  password: your_password
  
  # 连接池配置（可选）
  pool:
    max_size: 10
    min_size: 1
    max_inactive_connection_lifetime: 300
    
  # 时区配置（可选）
  timezone:
    use_tz: false
    timezone: Asia/Shanghai
```

```yaml
# 方式2：直接配置 URL
mysql:
  db_url: "mysql://username:password@localhost:3306/database"
  
  # 连接池配置（可选）
  pool:
    max_size: 10
    min_size: 1
    max_inactive_connection_lifetime: 300
```

## 使用示例

```python
from fastapi import FastAPI
from fastapi_utils.db import DBManager

app = FastAPI()

# 方式1：自动扫描实体
await DBManager.init_db(
    app=app,
    config="config/database.yaml",
    entity_dir="src/entity"
)

# 方式2：手动指定实体模块
await DBManager.init_db(
    app=app,
    config={
        "mysql": {
            "host": "localhost",
            "port": 3306,
            "database": "your_database",
            "username": "your_username",
            "password": "your_password"
        }
    },
    modules=[
        "src.entity.user_entity",
        "src.entity.product_entity"
    ]
)

# 方式3：混合使用
await DBManager.init_db(
    app=app,
    config="config/database.yaml",
    entity_dir="src/entity",
    modules=[
        "src.entity.special_entity"
    ]
)

# 数据库健康检查
is_healthy = await DBManager.health_check()
```

## 特性

1. 灵活的配置方式
   - 支持 YAML/JSON 配置文件
   - 支持直接传入配置字典
   - 支持 URL 方式和详细配置方式

2. 实体自动扫描
   - 自动扫描指定目录下的所有 `*_entity.py` 文件
   - 支持手动指定实体模块
   - 支持混合使用两种方式

3. 连接池配置
   - `max_size`: 最大连接数（默认：10）
   - `min_size`: 最小连接数（默认：1）
   - `max_inactive_connection_lifetime`: 连接最大空闲时间（秒）（默认：300）

4. 时区支持
   - `use_tz`: 是否使用时区（默认：false）
   - `timezone`: 时区设置（默认：Asia/Shanghai）

5. 健康检查
   - 提供数据库连接健康检查方法

## 注意事项

1. 实体文件命名必须以 `_entity.py` 结尾才能被自动扫描
2. 配置文件必须是 YAML 或 JSON 格式
3. 必须提供所有必需的数据库配置项（host、port、database 等）