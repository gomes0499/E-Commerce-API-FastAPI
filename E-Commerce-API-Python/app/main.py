from fastapi import FastAPI

app = FastAPI()

app.include_router(user.router, prefix="/api", tags=["users"])
