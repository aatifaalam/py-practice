from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return {}
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)    

app = FastAPI()
tasks = load_tasks()

class Task(BaseModel):
    title: str
    task_id: int

@app.get("/")
def home():
    return {"message": "Welcome to Task Tracker."}    

@app.post("/add_task")
def add_task(task: Task):
    tasks[task.title] = task.task_id
    save_tasks(tasks)
    return {"message": "Task added", "data": tasks}

@app.get("/get_task")
def get_task():
    return tasks
