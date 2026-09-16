from fastapi import FastAPI,HTTPException,status,Response
from pydantic import BaseModel

app = FastAPI()

# validation
class CreateTask(BaseModel):
    title: str
class UpdateTask(BaseModel):
    title: str | None = None
    done: bool | None = None

# database in memory
tasks: list[dict] = [
        {"id":1,"title":"shopping","done":True},
        {"id":2,"title":"cooking","done":False},
        {"id":3,"title":"studying","done":False}
        ]

# get operations
@app.get("/",status_code=status.HTTP_200_OK)
def root() -> dict:
    """ Return the root of the API """
    return {
            "name":"Task API", 
            "Version":"1.0",
            "endpoints":["/tasks"]
            }

@app.get("/health",status_code=status.HTTP_200_OK)
def health_check() -> dict:
    """ Check API health """
    return {"status":"ok"}

@app.get("/tasks",status_code=status.HTTP_200_OK)
def check_tasks(done: bool|None = None, search: str|None = None) -> list[dict]:
    """ Show all tasks or query or search """
    if done is not None:
        tasks_done = []
        for task in tasks:
            if task["done"] == done:
                tasks_done.append(task)
        return tasks_done
    if search is not None:
        tasks_search = []
        for task in tasks:
            if task["title"] == search:
                tasks_search.append(task)
        return tasks_search
    return tasks

@app.get("/tasks/{id}",status_code=status.HTTP_200_OK)
def get_specific_task(id: int) -> dict:
    """ Show specific task """
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"error":f"Task {id} not found"})

# post operation
@app.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_task(new_task: CreateTask) -> dict:
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

# put operations
@app.put("/tasks/{id}",status_code=status.HTTP_200_OK)
def update_task(id: int, updated_task: UpdateTask) -> dict:
    """ Update existing entry """
    for task in tasks:
        if task["id"] == id:
            if updated_task.done is not None:
                task["done"] = updated_task.done
            if updated_task.title is not None:
                if not updated_task.title.strip():
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="title can't be empty")
                task["title"] = updated_task.title.strip()
            return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Unknown id")

# delete operations
@app.delete("/tasks/{id}",status_code=status.HTTP_204_NO_CONTENT,response_class=Response)
def delete_task(id: int) -> None:
    """ Delete existing entry """
    for task in tasks:
        if task["id"] == id:
            index = tasks.index(task)
            tasks.pop(index)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Unknown id")

        