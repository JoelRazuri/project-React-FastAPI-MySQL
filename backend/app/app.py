from fastapi import FastAPI
from app.routers.user import user_router


app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World"}


# Routers
app.include_router(user_router, prefix="/api/users", tags=["users"])