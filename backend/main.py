from fastapi import FastAPI
from backend.api import login
from backend.scripts import create_users

app = FastAPI(title="Inventory Database Backend")


app.include_router(login.router)

create_users.create_demo_user()