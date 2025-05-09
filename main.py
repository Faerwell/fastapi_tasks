from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)