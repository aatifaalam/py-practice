from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"meassage": "Hello, Aatif"}

# users = {}
# number_of_users = int(input("Enter numbers of users: "))
# @app.get("/add-users")
# def add_users(users):
#     for i in range(number_of_users):
#         name = input("Enter name: ")
#         id = int(input("Enter id: "))
#         users[name] = id 
#         return {"message": "User Added!"}

users = {}
@app.get("/add_users")
def add_users(name: str, age: int):
    users[name] = age
    return {"message": "User Added"}
      

@app.get("/get_user")
def get_users(users):
    return users

@app.get("/user/{name}")
def get_user(name: str):
    if name in users:
        return {name: users[name]}
    return {"error": "User not found"}

@app.get("/update_user/{name}")
def update_user(name: str, age: int):
    users.update({name:age})
    return {"meassage": "User Updated"}, users

@app.get("/home")
def hello():
    return {"message": "Hello, Aatif! Welcome to FastAPI"}