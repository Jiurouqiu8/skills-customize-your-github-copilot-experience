from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

tasks: List[Task] = [
    Task(id=1, title="Learn FastAPI", description="Read the FastAPI documentation", completed=False),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI task manager"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    if not task.title or task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title is required")

    tasks.append(task)
    return task
