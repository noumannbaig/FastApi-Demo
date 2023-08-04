from fastapi import FastAPI,APIRouter
from api.views import user_router

app = FastAPI()
api_router = APIRouter()

api_router.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)
