from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def hello():
    return {"message": "Hello, Aatif! Welcome to FastAPI"}