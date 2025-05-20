## FastAPI 基本路由

FastAPI 基本路由
在 FastAPI 中，基本路由是定义 API 端点的关键。每个路由都映射到应用程序中的一个函数，用于处理特定的 HTTP 请求，并返回相应的响应。

### 根路径路由
创建 FastAPI 实例和根路径路由：

实例
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
代码说明：

FastAPI()：创建 FastAPI 应用实例。
@app.get("/")：使用 @app.get 装饰器创建一个处理根路径的路由。
def read_root()：路由处理函数，返回一个包含 {"Hello": "World"} 的字典。
### 路径参数
设置路由的参数：

实例
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
代码说明：

@app.get("/items/{item_id}")：定义了一个路由路径，其中 {item_id} 是路径参数，对应于函数参数 item_id。
def read_item(item_id: int, q: str = None)：路由处理函数接受一个整数类型的路径参数 item_id 和一个可选的字符串类型查询参数 q。
在路由操作中，可以使用函数参数声明查询参数。例如，q: str = None 表示 q 是一个可选的字符串类型查询参数，默认值为 None。

### 启动应用和测试路由
使用 Uvicorn 启动应用：

uvicorn main:app --reload
访问 http://127.0.0.1:8000 查看根路径的响应：



访问 http://127.0.0.1:8000/items/42?q=runoob 查看带路径参数和查询参数的响应：



FastAPI 自动生成的交互式 API 文档将包括定义的路由信息、路径参数、查询参数等。访问文档地址 http://127.0.0.1:8000/docs 查看详细的文档和测试界面：



