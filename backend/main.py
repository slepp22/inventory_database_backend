from fastapi import FastAPI

app = FastAPI(title="Inventory Database Backend")


@app.get("/")
async def root():
    return {"message": "Hello World2"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
