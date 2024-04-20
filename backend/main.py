from fastapi import FastAPI
from backend.api import login

app = FastAPI(title="Inventory Database Backend")


app.include_router(login.router)