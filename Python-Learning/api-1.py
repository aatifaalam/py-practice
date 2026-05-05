from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"meassage": "Hello, Aatif"}

@app.get("/home")
def hello():
    return {"message": "Hello, Aatif! Welcome to FastAPI"}