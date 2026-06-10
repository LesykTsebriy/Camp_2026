import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/greet")
def greet_api(name: str, intensity: int):
    """The core engine logic that processes requests"""
    result_string = ("Hello " * intensity) + name + "!"
    return {"result": result_string}

if __name__ == "__main__":
    # Starts the API server on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
