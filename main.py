from fastapi import FastAPI, status, HTTPException, Depends
from google.cloud import bigquery


def get_bq_client():
    client = bigquery.Client()
    try:
        yield client
    finally:
        client.close()


app = FastAPI()


@app.get("/", status_code=200)
def health():
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}


@app.get("/power/{a}/{b}", status_code=200)
def power(a: float, b: float):
    return {"result": a ** b}


@app.get("/triangle/{base}/{height}", status_code=200)
def triangle(base: float, height: float):
    return {"result": (base * height) / 2}


@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: float, b: float, c: float):
    return {"result": (a + b + c) / 3}


@app.get("/dbwritetest", status_code=200)
def dbwritetest(bq: bigquery.Client = Depends(get_bq_client)):
    row_to_insert = [
        {
            "endpoint": "/dbwritetest",
            "result": "Success",
            "status_code": 200
        }
    ]

    errors = bq.insert_rows_json("leafy-clone-452120-b6.calculator.request_logs", row_to_insert)

    if errors:
        print(f"BigQuery Insert Errors: {errors}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Failed to log data to BigQuery",
                "errors": errors
            }
        )

    return {"message": "Log entry created successfully"}
