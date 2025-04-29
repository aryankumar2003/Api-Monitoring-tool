# FastAPI Metrics Monitoring

A simple FastAPI application with Prometheus metrics integration and Grafana dashboards for monitoring API performance.

## Overview

This project demonstrates how to set up monitoring for a FastAPI application using:

- **FastAPI**: Modern, fast web framework for building APIs
- **Prometheus**: Time series database for metrics collection
- **Grafana**: Visualization platform for creating dashboards

The sample API includes several endpoints to simulate real-world scenarios including normal operation, random failures, and variable latency responses.

## Features

- FastAPI application with sample endpoints
- Prometheus metrics integration
- Request count and latency monitoring
- Docker Compose setup for easy deployment
- Grafana dashboard for visualization

## Project Structure

```
.
├── app/
│   └── main.py                # FastAPI application code
├── grafana/
│   └── dashboards/
│       └── api_metrics.json   # Grafana dashboard configuration
├── Dockerfile                 # Docker configuration for API
├── docker-compose.yml         # Docker Compose configuration
├── prometheus.yml             # Prometheus configuration
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Metrics Collected

- **request_count**: Total number of requests (labeled by method, endpoint, and HTTP status)
- **request_latency_seconds**: Latency of requests in seconds (labeled by endpoint)

## API Endpoints

- **GET /health**: Health check endpoint
- **GET /data**: Simulated data endpoint with variable latency (0.1-1.5s)
- **GET /fail**: Endpoint that randomly fails ~30% of the time
- **GET /metrics**: Prometheus metrics endpoint

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Running the Application

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Start the services:
   ```
   docker-compose up -d
   ```

3. Access the services:
   - FastAPI application: http://localhost:8000
   - Prometheus UI: http://localhost:9090
   - Grafana: http://localhost:3000

### Setting up Grafana

1. Log in to Grafana (http://localhost:3000) with default credentials:
   - Username: `admin`
   - Password: `admin`

2. Add Prometheus as a data source:
   - Go to Configuration > Data Sources > Add data source
   - Select Prometheus
   - Set URL to `http://prometheus:9090`
   - Click "Save & Test"

3. Import the dashboard:
   - Go to Create > Import
   - Upload the JSON file from `grafana/dashboards/api_metrics.json` or create your own dashboard

## Testing the Application

Generate some traffic to test the metrics collection:

```bash
# Health endpoint
curl http://localhost:8000/health

# Data endpoint (with variable latency)
curl http://localhost:8000/data

# Endpoint with random failures
curl http://localhost:8000/fail

# View raw metrics
curl http://localhost:8000/metrics
```

## Development

### Extending the API

To add new endpoints, modify `app/main.py` and add your routes. The metrics middleware will automatically track requests.

### Customizing Metrics

To add custom metrics:

1. Define new metrics in `app/main.py`
2. Update the middleware or specific endpoints to record these metrics
3. Adjust your Grafana dashboard to visualize the new metrics

## License

[MIT License](LICENSE)
