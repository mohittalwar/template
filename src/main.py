from fastapi import FastAPI
import utils


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": utils.get_message()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None) -> dict[str, int | str]:
    return {"item_id": item_id, "q": f"{q}" if q else "None"}


if __name__ == "__main__":
    print(utils.get_message())
