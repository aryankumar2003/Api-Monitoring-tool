from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/data")
def get_data():
    time.sleep(random.uniform(0.1, 1.5))  # Simulate latency
    return {"data": "sample"}

@app.get("/fail")
def fail_randomly():
    if random.random() < 0.3:
        raise Exception("Simulated error")
    return {"status": "success"}
