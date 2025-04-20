from fastapi import FastAPI, Request
from starlette.responses import Response
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = FastAPI()

# Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests", ["method", "endpoint", "http_status"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Latency of requests in seconds", ["endpoint"])

# Middleware to capture metrics
@app.middleware("http")
async def add_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(process_time)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path, http_status=response.status_code).inc()
    return response

# Health endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Simulated data endpoint
@app.get("/data")
def get_data():
    time.sleep(random.uniform(0.1, 1.5))  # Simulate latency
    return {"data": "sample"}

# Simulated failure endpoint
@app.get("/fail")
def fail_randomly():
    if random.random() < 0.3:
        raise Exception("Simulated error")
    return {"status": "success"}

# Prometheus metrics endpoint
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
