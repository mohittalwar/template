from fastapi import FastAPI
from hello import Hello


app = FastAPI()


@app.get("/")
async def root():
    return {"message": Hello().get_message()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
