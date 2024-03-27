from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    password: str
    username: str
    email: str

@app.post("/user")
    async def root(user):
    return {user}