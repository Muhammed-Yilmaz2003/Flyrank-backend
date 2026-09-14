from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """ returns the root of the API """
    return {
            "name":"Task API", 
            "Version":"1.0",
            "endpoints":["/tasks"]
            }

@app.get("/health")
def health_check():
    """ Checks API health """
    return {"status":"ok"}
