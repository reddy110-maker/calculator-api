from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "healthy"}

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"result": a - b}