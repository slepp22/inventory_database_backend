from fastapi import FastAPI, APIRouter

app = FastAPI(title="inventory_database_api")

api_router = APIRouter()


@api_router.get("/")
def home():
    return "Hello, World!"


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
