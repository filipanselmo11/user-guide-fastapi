from fastapi import FastAPI, Query
from typing_extensions import Annotated
from typing import Union, List

app = FastAPI()

#Pydantic v1 regex instead of pattern
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3,max_length=50, regex="^fixedquery$")] = None,):
    results = {
        "items":
            [
                {"item_id": "Foo"},
                {"item_id": "Bar"}
            ]
    }

    if q:
        results.update({"q": q})
    return results

#Default Values
@app.get("/items-2/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

# Required with Ellipsis(...)
@app.get("/items-3/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Required with None
@app.get("/items-3/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
    results = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Query parameter list/multiple values
@app.get("/items-4/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q":q}
    return query_items

#Query parameter list/multiple values with defaults
@app.get("/items-5/")
async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

#Using list
@app.get("/items-6/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items

#Declare More Metadata
@app.get("/items-7/")
async def read_items(
    q: Annotated[Union[str, None], Query(title="Olá, eu sou o Fílip", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Add description
@app.get("/items-8/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#Alias parameters
@app.get("/items-9/")
async def read_items(q: Annotated[Union[str, None], Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Deprecating parameters
@app.get("/items-10/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Exclude from openAPi
@app.get("/items-11/")
async def read_items(
    hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}