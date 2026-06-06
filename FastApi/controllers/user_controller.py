from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.user_service import (
add_user,
get_all_users,
get_user_by_name
)

router = APIRouter()

class User(BaseModel):
    name: str
    hobby: str

@router.get("/")
def home():
    return {
        "message": "Welcome! Your FastAPI server is running successfully."
    }

@router.post("/add-user")
def create_user(user: User):
    data = add_user(user.name, user.hobby)

    return {
        "message": "User Added",
        "data": data
    }

@router.get("/get_users")
def get_users():
    return get_all_users()

@router.get("/user_by_name/{name}")
def find_user(name: str):
    hobby = get_user_by_name(name)

    if hobby is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "name": name,
        "hobby": hobby
    }

