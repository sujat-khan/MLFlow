FROM python:3.10-slim

LABEL maintainer="MLFlow Learn Course"
LABEL description="Wine Quality Classifier — MLFlow Model Server"

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    mlflow>=2.15.0 \
    scikit-learn>=1.5.0 \
    pandas>=2.2.0 \
    numpy>=1.26.0

# Copy model from local MLFlow artifacts
# Replace <RUN_ID> with your actual run ID
# COPY mlartifacts/<experiment_id>/<run_id>/artifacts/model /opt/model

# Set environment variables
ENV MLFLOW_MODEL_URI=/opt/model
ENV PORT=8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD curl -f http://localhost:${PORT}/ping || exit 1

# Expose port
EXPOSE ${PORT}

# Start the model server
CMD ["sh", "-c", "mlflow models serve -m ${MLFLOW_MODEL_URI} -h 0.0.0.0 -p ${PORT} --no-conda"]
