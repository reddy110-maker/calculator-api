from fastapi import FastAPI, HTTPException


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

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    if b ==0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")    
    return {"result": a / b}

@app.get("/power/{a}/{b}")
def power(a: float, b: float):
    return {"result": a ** b}

@app.get("/triangle/{base}/{height}")
def triangle(base: float, height: float):
    return {"result": (base * height)/2}

@app.get("/rectangle/{length}/{width}")
def square(a: float):
    return {"result": a ** 2}

@app.get("/average/{a}/{b}/{c}")
def average(a: float, b: float, c: float):
    return {"result": (a + b + c)/3}
