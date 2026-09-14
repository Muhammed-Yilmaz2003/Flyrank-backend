from fastapi import FastAPI,HTTPException

app = FastAPI()

tasks = [
        {"id":1,"title":"shopping","done":True},
        {"id":2,"title":"cooking","done":False},
        {"id":3,"title":"studying","done":False}
        ]

@app.get("/")
def root() -> dict:
    """ returns the root of the API """
    return {
            "name":"Task API", 
            "Version":"1.0",
            "endpoints":["/tasks"]
            }

@app.get("/health")
def health_check() -> dict:
    """ Checks API health """
    return {"status":"ok"}

@app.get("/tasks")
def check_tasks() -> list:
    """ Shows all tasks """
    return tasks

@app.get("/tasks/{id}")
def get_specific_task(id: int) -> dict:
    """ Shows specific task """
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404,detail={"error":f"Task {id} not found"})

