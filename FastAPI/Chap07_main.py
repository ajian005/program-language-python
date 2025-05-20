from pydantic import BaseModel
from fastapi import FastAPI, Query

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price:float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/items/")
def read_item(item: Item, q: str = Query(..., max_length=10)):
    return {"item": item, "q": q}