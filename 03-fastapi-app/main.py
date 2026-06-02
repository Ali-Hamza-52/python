from fastapi import FastAPI
from fastapi import status

app = FastAPI()
# Simple / web API with FastAPI
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path parameter example
@app.get("/items/{item_id}")
def read_items(item_id:int):
    return {"item_id": item_id}

# Query parameter example
@app.get("/items")
def read_items_query(search: str = None, limit: int = 10):
    return {"search": search, "limit": limit}

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(name: str, price: float):
    return {"name": name, "price": price}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str = None, price: float = None):
    return {"item_id": item_id, "name": name, "price": price}

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return {"item_id": item_id}

@app.patch("/items/{item_id}")
def patch_item(item_id: int, name: str = None, price: float = None):
    return {"item_id": item_id, "name": name, "price": price}
def main():
    print("Hello from 03-fastapi-app!")


if __name__ == "__main__":
    main()
