# Module 8.5: Remote Tracking Server

## 🎯 Goal

Set up a **remote MLFlow tracking server** that multiple users/machines can connect to.

---

## Architecture

```
Data Scientist A ──┐
                    ├──▶ MLFlow Tracking Server ──▶ PostgreSQL (metadata)
Data Scientist B ──┘         │
                             └──▶ S3 / Local (artifacts)
```

---

## Option 1: Local Network Server

Run the server on a machine accessible to your team.

### Server Setup

```bash
# Start PostgreSQL (Docker)
docker run -d \
  --name mlflow-postgres \
  -e POSTGRES_USER=mlflow \
  -e POSTGRES_PASSWORD=mlflow123 \
  -e POSTGRES_DB=mlflow_db \
  -p 5432:5432 \
  postgres:15

# Start MLFlow server
mlflow server \
  --backend-store-uri postgresql://mlflow:mlflow123@localhost:5432/mlflow_db \
  --default-artifact-root ./mlartifacts \
  --host 0.0.0.0 \
  --port 5000
```

> **`--host 0.0.0.0`** makes the server accessible from other machines on the network.

### Client Setup

On any machine that needs to connect:

```python
import mlflow
mlflow.set_tracking_uri("http://<SERVER_IP>:5000")

# Now all MLFlow operations go to the remote server
mlflow.set_experiment("my_experiment")
with mlflow.start_run():
    mlflow.log_param("hello", "world")
```

---

## Option 2: AWS S3 Artifact Store

For larger teams, store artifacts in S3:

```bash
mlflow server \
  --backend-store-uri postgresql://mlflow:mlflow123@localhost:5432/mlflow_db \
  --default-artifact-root s3://my-mlflow-bucket/artifacts \
  --host 0.0.0.0 \
  --port 5000
```

### Requirements:
- AWS credentials configured on the server
- S3 bucket created and accessible
- `boto3` installed: `pip install boto3`

---

## Option 3: Docker Compose (All-in-One)

Create a `docker-compose.yml` for the full stack:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: mlflow
      POSTGRES_PASSWORD: mlflow123
      POSTGRES_DB: mlflow_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  mlflow:
    image: python:3.10-slim
    depends_on:
      - postgres
    ports:
      - "5000:5000"
    volumes:
      - mlflow_artifacts:/mlflow/artifacts
    command: >
      bash -c "pip install mlflow psycopg2-binary &&
      mlflow server
      --backend-store-uri postgresql://mlflow:mlflow123@postgres:5432/mlflow_db
      --default-artifact-root /mlflow/artifacts
      --host 0.0.0.0
      --port 5000"

volumes:
  postgres_data:
  mlflow_artifacts:
```

### Run:

```bash
docker-compose up -d
```

This gives you a complete MLFlow server with PostgreSQL — no manual installation needed.

---

## Security Considerations

| Concern | Solution |
|---------|----------|
| **Authentication** | Use a reverse proxy (nginx) with basic auth or OAuth |
| **HTTPS** | Add SSL certificates to nginx |
| **Network** | Use private subnets, VPN, or security groups |
| **Secrets** | Use environment variables, never hardcode passwords |

### Example Nginx Config for Basic Auth

```nginx
server {
    listen 80;
    server_name mlflow.yourdomain.com;

    location / {
        auth_basic "MLFlow";
        auth_basic_user_file /etc/nginx/.htpasswd;
        proxy_pass http://localhost:5000;
    }
}
```

---

## Multi-User Best Practices

1. **Naming conventions**: Use team/project prefixes for experiments
2. **Tags**: Always tag runs with `mlflow.set_tag("author", "your_name")`
3. **Access control**: Use proxy-based authentication
4. **Artifact storage**: Use S3/GCS for shared artifact access
5. **Backup**: Schedule regular PostgreSQL backups with `pg_dump`

---

## 🔑 Key Takeaways

1. **`--host 0.0.0.0`** makes the server network-accessible
2. **PostgreSQL + S3** is the production-grade setup
3. **Docker Compose** simplifies the entire stack
4. Add **authentication** via a reverse proxy for security
5. Use **naming conventions** and **tags** for multi-user collaboration

---

## ➡️ Next: `06_exercises.ipynb`
