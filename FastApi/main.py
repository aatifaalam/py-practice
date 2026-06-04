from fastapi import FastAPI
import json
from pydantic import BaseModel
from fastapi import HTTPException

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_users(user):
    with open("users.json", "w") as file:
        json.dump(user, file)

app = FastAPI()
users = load_users()

class User(BaseModel):
    name: str
    hobby: str

@app.get("/")
def home():
    return {"message": "Welcome! Your FastAPI server is running successfully."}

@app.post("/add-user")
def add_user(user: User):
    users[user.name] = user.hobby
    save_users(users)
    return {"message": "User Added", "data": users}

@app.get("/get_users")
def get_users():
    return users


# So now I want to find user by name, like when I typr user's anme it shoild show its hobby
@app.get("/user_by_name/{name}")
def get_user_by_name(name: str):
    if name not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
            "name": name,
            "hobby": users[name]
        }