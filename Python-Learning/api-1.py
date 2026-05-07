from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {}
class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return "Welcome Aatif, FastAPI is running."

@app.post("/add_user")
def add_user(user: User):
    users[user.name] = user.age
    return {"message": "User added", "data": users}

@app.get("/users")
def get_users():
    return users

@app.get("/user/{name}")
def get_user(name: str):
    if name not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {name: users[name]}

@app.put("/update_user/{name}")
def update_user(name: str, user: User):
    if name not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[name] = user.age
    return {"message": "User updated", "data": users}

@app.delete("/delete_user/{name}")
def delete_user(name: str):
    if name not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[name]
    return {"mesaage": "Deleted", "data": users}