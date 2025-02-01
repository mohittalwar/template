from fastapi import FastAPI
from hello import Hello


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": Hello().get_message()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None) -> dict[str, int | str]:
    return {"item_id": item_id, "q": f"{q}" if q else "None"}


if __name__ == "__main__":
    print(Hello().get_message())
