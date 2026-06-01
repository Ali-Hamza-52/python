# Setup FastAPI application with uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "Hey, This is Ali Hamza"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}