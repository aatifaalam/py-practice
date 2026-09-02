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

@router.put("/update_user/{name}")
def update_user(name: str, user: User):
    hobby = get_user_by_name(name)

    if hobby is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    data = add_user(name, user.hobby)

    return {
        "message": "User Updated",
        "data": data
    }

@router.delete("/delete_user/{name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(name: str):
    hobby = get_user_by_name(name)

    if hobby is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    data = add_user(name, "")

    return {
        "message": "User Deleted",
        "data": data
    }