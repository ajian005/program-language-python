"""
以下的 FastAPI 应用，使用了两个路由操作（/ 和 /items/{item_id}）：

"""
from fastapi import FastAPI
from typing  import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}