# Module 7: Deployment — Docker & AWS 🚀

## 🎯 Learning Objectives

By the end of this module, you will:
- Serve MLFlow models locally as a **REST API**
- Build **Docker containers** from MLFlow models
- Deploy to **AWS** using ECR and SageMaker/EC2
- Understand deployment strategies (batch vs real-time)

---

## 1. Deployment Strategies

| Strategy | Latency | Use Case | MLFlow Support |
|----------|---------|----------|----------------|
| **Local REST API** | Low (dev) | Testing, prototyping | `mlflow models serve` |
| **Docker Container** | Low | Microservices, Kubernetes | `mlflow models build-docker` |
| **AWS SageMaker** | Low | Production real-time | `mlflow.sagemaker` |
| **Batch Scoring** | High | Bulk predictions | `mlflow.pyfunc.load_model()` + script |

---

## 2. Local Serving

```bash
# Serve a model from a run
mlflow models serve -m runs:/<run_id>/model -p 1234 --no-conda

# Serve from model registry
mlflow models serve -m models:/wine-quality-classifier@champion -p 1234 --no-conda
```

### REST API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/invocations` | POST | Make predictions |
| `/ping` | GET | Health check |
| `/version` | GET | MLFlow version |

### Request Format

```json
{
  "dataframe_split": {
    "columns": ["feature_1", "feature_2"],
    "data": [[1.0, 2.0], [3.0, 4.0]]
  }
}
```

---

## 3. Docker Deployment

```bash
# Build Docker image from a model
mlflow models build-docker \
  -m runs:/<run_id>/model \
  -n wine-quality-model \
  --enable-mlserver

# Run the container
docker run -p 8080:8080 wine-quality-model
```

---

## 4. AWS Deployment Overview

```
Your MLFlow Model
    │
    ▼
Docker Image (mlflow models build-docker)
    │
    ▼
AWS ECR (Container Registry)
    │
    ├──▶ SageMaker Endpoint (managed, auto-scaling)
    │
    └──▶ EC2 Instance (self-managed, more control)
```

---

## ⚠️ AWS Cost Warning

> **The AWS free tier covers limited SageMaker and EC2 usage.** Always clean up resources after testing to avoid unexpected charges. The notebooks include cleanup steps.

---

## ➡️ Next Steps

1. `02_local_serving.ipynb` — Serve models locally
2. `03_docker_containerization.ipynb` — Build Docker images
3. `04_aws_deployment.ipynb` — Deploy to AWS
