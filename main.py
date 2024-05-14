from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/items/")
async def read_items(skip: int = 0, limit : int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None):
    if (q):
        return {"item_id":item_id, "q":q}
    return {"item_id":item_id}

@app.get("/items/{item_id_2}")
async def read_item(item_id_2: str, q: str | None = None, short: bool = False):
    item = {"item_id_2":item_id_2}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "this is an amazing item that has a long description"}

        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "this is an amazing item that has a long description"}
        )
    return item


@app.get("/items/{item_id_3}")
async def read_user_item(item_id_3: str, needy: str):
    item = {"item_id":item_id_3, "needy": needy}
    return item