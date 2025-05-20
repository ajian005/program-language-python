## FastAPI 路径操作依赖项
FastAPI 提供了简单易用，但功能强大的依赖注入系统，这个依赖系统设计的简单易用，可以让开发人员轻松地把组件集成至 FastAPI。

FastAPI 提供了路径操作依赖项（Path Operation Dependencies）的机制，允许你在路由处理函数执行之前或之后运行一些额外的逻辑。

依赖项就是一个函数，且可以使用与路径操作函数相同的参数。

路径操作依赖项提供了一种灵活的方式来组织代码、验证输入、进行身份验证等。

接下来我们会具体介绍 FastAPI 路径操作依赖项的相关知识点。

## 1、依赖项（Dependencies）
依赖项是在路由操作函数执行前或后运行的可复用的函数或对象。

它们被用于执行一些通用的逻辑，如验证、身份验证、数据库连接等。在 FastAPI 中，依赖项通常用于两个方面：

预处理（Before）依赖项： 在路由操作函数执行前运行，用于预处理输入数据，验证请求等。
后处理（After）依赖项： 在路由操作函数执行后运行，用于执行一些后处理逻辑，如日志记录、清理等。
### 1.1 依赖注入
依赖注入是将依赖项注入到路由操作函数中的过程。

在 FastAPI 中，通过在路由操作函数参数中声明依赖项来实现依赖注入。

FastAPI 将负责解析依赖项的参数，并确保在执行路由操作函数之前将其传递给函数。

### 1.2 依赖项的使用
定义依赖项：

实例
```python
from fastapi import Depends, FastAPI

app = FastAPI()

# 依赖项函数
def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
```
在这个例子中，common_parameters 是一个依赖项函数，用于预处理查询参数。

在路由中使用依赖项：

实例
```python
from fastapi import Depends

# 路由操作函数
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
```
在这个例子中，read_items 路由操作函数中的参数 commons 使用了 Depends(common_parameters)，表示 common_parameters 是一个依赖项。FastAPI 将在执行路由操作函数之前运行 common_parameters 函数，并将其返回的结果传递给 read_items 函数。

## 2、路径操作依赖项的基本使用
### 2.1 预处理（Before）
以下实例中，common_parameters 是一个依赖项函数，它接受查询参数 q、skip 和 limit，并返回一个包含这些参数的字典。

在路由操作函数 read_items 中，通过传入 Depends(common_parameters)，我们使用了这个依赖项函数，实现了在路由执行前预处理输入数据的功能。

实例
```python
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

# 依赖项函数
def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# 路由操作函数
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
```
### 2.2 后处理（After）
以下例子中，after_request 是一个后处理函数，用于在路由执行后执行一些逻辑。

在路由操作函数 read_items_after 中，通过传入 Depends(after_request)，我们使用了这个后处理依赖项，实现了在路由执行后进行额外操作的功能。

实例
```python
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

# 依赖项函数
def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# 路由操作函数
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

# 后处理函数
async def after_request():
    # 这里可以执行一些后处理逻辑，比如记录日志
    pass

# 后处理依赖项
@app.get("/items/", response_model=dict)
async def read_items_after(request: dict = Depends(after_request)):
    return {"message": "Items returned successfully"}
```
## 3、多个依赖项的组合
以下例子中，common_parameters 和 verify_token 是两个不同的依赖项函数，verify_token 依赖于 common_parameters，这种组合依赖项的方式允许我们在路由执行前先验证一些参数，然后在进行身份验证。

实例
```python
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

# 依赖项函数1
def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# 依赖项函数2
def verify_token(token: str = Depends(common_parameters)):
    if token is None:
        raise HTTPException(status_code=400, detail="Token required")
    return token

# 路由操作函数
@app.get("/items/")
async def read_items(token: dict = Depends(verify_token)):
    return token
```
## 4、异步依赖项
依赖项函数和后处理函数可以是异步的，允许在它们内部执行异步操作。

以下例子中，get_token 是一个异步的依赖项函数，模拟了一个异步操作。

在路由操作函数 read_items 中，我们使用了这个异步依赖项函数。

实例
```python
from fastapi import Depends, FastAPI, HTTPException
from typing import Optional
import asyncio

app = FastAPI()

# 异步依赖项函数
async def get_token():
    # 模拟异步操作
    await asyncio.sleep(2)
    return "fake-token"

# 异步路由操作函数
@app.get("/items/")
async def read_items(token: Optional[str] = Depends(get_token)):
    return {"token": token}
```
通过使用路径操作依赖项，你可以在路由执行前或后执行额外的逻辑，从而实现更灵活、可组合的代码组织方式。