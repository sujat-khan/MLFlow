# 🚀 MLFlow End-to-End Course

A comprehensive, hands-on course to master **MLFlow** — from basic experiment tracking to production deployment with Docker & AWS.

---

## 📋 Prerequisites

- **Python 3.10+** installed
- **Docker Desktop** installed and running
- **AWS Free Tier** account (for Module 7)
- Basic knowledge of **machine learning** concepts (classification, regression, train/test split)
- Familiarity with **scikit-learn** (helpful but not required)

---

## 🗂️ Course Modules

| # | Module | What You'll Learn |
|---|--------|-------------------|
| 1 | **Introduction** | What is MLFlow & MLOps, installation, your first experiment |
| 2 | **Tracking** | Log parameters, metrics, artifacts — the core MLFlow API |
| 3 | **Experiments & UI** | Organize work, search/compare runs, master the MLFlow UI |
| 4 | **Model Registry** | Model versioning, aliases, champion/challenger workflows |
| 5 | **MLFlow Models** | Model flavors, signatures, custom PyFunc models, evaluation |
| 6 | **MLFlow Projects** | Reproducible ML with MLproject files |
| 7 | **Deployment** | Local serving → Docker → AWS (ECR + SageMaker) |
| 8 | **Advanced Topics** | Hyperparameter tuning (Optuna), pipelines, PostgreSQL backend |
| 9 | **Capstone Project** | End-to-end ML project combining all modules |

---

## 🛠️ Getting Started

### 1. Clone / Open this folder

```bash
cd c:\Users\sujat\projects\MLFlow_Learn
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Register the Jupyter kernel

```bash
python -m ipykernel install --user --name=mlflow_learn --display-name "MLFlow Learn"
```

### 5. Launch Jupyter

```bash
jupyter notebook
```

### 6. Start the MLFlow UI (in a separate terminal)

```bash
cd c:\Users\sujat\projects\MLFlow_Learn
venv\Scripts\activate
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📖 How to Use This Course

1. **Start with Module 1** and work through modules sequentially — each builds on the previous
2. Within each module:
   - Read `01_theory.md` first for concepts
   - Work through the numbered notebooks in order
   - Complete the exercises notebook at the end
3. **Keep the MLFlow UI open** while working through notebooks — you'll frequently check it to see your logged data
4. Each notebook includes:
   - 📝 **Markdown explanations** above each code cell
   - 💡 **Key takeaways** at the end
   - 🎯 **Learning objectives** at the top

---

## 📊 Dataset

This course primarily uses the **Wine Quality** dataset from scikit-learn / UCI ML Repository.
- Binary classification: predict wine quality (good vs. not good)
- 11 numerical features (acidity, sugar, pH, alcohol, etc.)
- Clean, well-understood, no preprocessing headaches — so you can focus on MLFlow

---

## ⚡ Quick Reference

| Command | Purpose |
|---------|---------|
| `mlflow ui` | Launch the tracking UI on port 5000 |
| `mlflow server --backend-store-uri sqlite:///mlflow.db` | Start server with SQLite backend |
| `mlflow models serve -m runs:/<run_id>/model -p 1234` | Serve a model locally |
| `mlflow models build-docker -m runs:/<run_id>/model -n my-model` | Build a Docker image |
| `mlflow.search_runs()` | Query runs programmatically |

---

*Built with ❤️ for learning MLOps*
