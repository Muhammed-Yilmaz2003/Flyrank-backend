from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

app = FastAPI()

class CreateTask(BaseModel):
    title: str

tasks: list[dict] = [
        {"id":1,"title":"shopping","done":True},
        {"id":2,"title":"cooking","done":False},
        {"id":3,"title":"studying","done":False}
        ]

@app.get("/",status_code=status.HTTP_200_OK)
def root() -> dict:
    """ Returns the root of the API """
    return {
            "name":"Task API", 
            "Version":"1.0",
            "endpoints":["/tasks"]
            }

@app.get("/health",status_code=status.HTTP_200_OK)
def health_check() -> dict:
    """ Checks API health """
    return {"status":"ok"}

@app.get("/tasks",status_code=status.HTTP_200_OK)
def check_tasks() -> list:
    """ Shows all tasks """
    return tasks

@app.get("/tasks/{id}",status_code=status.HTTP_200_OK)
def get_specific_task(id: int) -> dict:
    """ Shows specific task """
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"error":f"Task {id} not found"})

@app.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_task(new_task: CreateTask):
    """ Create a new task """
    if not new_task.title.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="empty task title")
    task_ids = []
    for task in tasks:
        task_ids.append(task["id"])
    new_id = max(task_ids,default=0)+1
    created_task = {
        "id":new_id,
        "title":new_task.title.strip(),
        "done":False}
    tasks.append(created_task)
    return created_task

