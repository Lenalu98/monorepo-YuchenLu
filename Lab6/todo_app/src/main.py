from fastapi import FastAPI, Path, Query

app = FastAPI()

# GET ReST API
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# GET ReST API with path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# GET ReST API with query parameters
@app.get("/items/")
async def read_items(skip: int = Query(0, title="Skip items", description="Number of items to skip")):
    return {"skip": skip}

# GET ReST API with path parameters AND query parameters
@app.get("/items_with_query/{item_id}")
async def read_items_with_query(item_id: int, skip: int = Query(0, title="Skip items", description="Number of items to skip")):
    return {"item_id": item_id, "skip": skip}

# POST ReST API
@app.post("/items/")
async def create_item(item: dict):
    return item

# PUT ReST API
@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: dict):
    return {"item_id": item_id, "updated_item": updated_item}

# DELETE ReST API
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}
