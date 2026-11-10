"""Starter code for the FastAPI REST API assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Tracker API", version="1.0.0")


class TaskCreate(BaseModel):
    title: str
    description: str = ""


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: dict[int, Task] = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Tracker API"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all tasks.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    # TODO: Create a task with the next available ID, store it, and return it.
    raise NotImplementedError


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    # TODO: Update only the provided fields, or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the task and return a confirmation, or raise HTTPException with status 404.
    raise NotImplementedError
