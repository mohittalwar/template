from fastapi import FastAPI

import config
import utils

settings = config.get_settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": utils.get_message()}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    print(utils.get_message())
