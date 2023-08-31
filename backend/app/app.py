from fastapi import FastAPI
from app.routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = [
    "http://localhost:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def hello():
    return {"message": "Hello World"}


# Routers
app.include_router(user_router, prefix="/api/users", tags=["users"])