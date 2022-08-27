from fastapi import FastAPI, HTTPException
from controller import client_controller

app = FastAPI()
app.include_router(client_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def test_connection():
    return {"healthy": "health"}
