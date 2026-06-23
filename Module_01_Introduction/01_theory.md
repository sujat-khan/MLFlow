# Module 1: Introduction to MLFlow & MLOps

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand what **MLOps** is and why it matters
- Know the **4 core components** of MLFlow
- Have a **working MLFlow installation** on your machine
- Complete your **first MLFlow experiment** — training a model and viewing results in the UI

---

## 1. What is MLOps?

**MLOps** (Machine Learning Operations) is a set of practices that combines **Machine Learning**, **DevOps**, and **Data Engineering** to deploy and maintain ML systems in production reliably and efficiently.

### The ML Lifecycle Problem

Without MLOps, data scientists face these pain points:

```
😩 "Which version of my model was the best?"
😩 "What hyperparameters did I use for that good result 3 weeks ago?"
😩 "It works on my laptop — why not in production?"
😩 "How do I roll back to the previous model version?"
😩 "Who trained this model and with what data?"
```

MLOps solves these by bringing **software engineering discipline** to ML:

| Practice | What It Solves |
|----------|---------------|
| **Experiment Tracking** | "What did I try and what worked?" |
| **Model Versioning** | "Which model is in production?" |
| **Reproducibility** | "Can someone else reproduce my results?" |
| **Deployment Automation** | "How do I get this model to users?" |
| **Monitoring** | "Is my model still performing well?" |

---

## 2. What is MLFlow?

**MLFlow** is an **open-source platform** for managing the end-to-end ML lifecycle. Created by **Databricks** in 2018, it's become the most widely adopted MLOps tool.

### The 4 Components of MLFlow

```
┌─────────────────────────────────────────────────────────┐
│                       MLFlow                             │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Tracking    │  │   Projects   │  │    Models     │  │
│  │              │  │              │  │              │  │
│  │ Log params,  │  │ Package code │  │ Standard     │  │
│  │ metrics,     │  │ for repro-   │  │ format for   │  │
│  │ artifacts    │  │ ducibility   │  │ deployment   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Model Registry                       │   │
│  │  Central hub to manage model lifecycle            │   │
│  │  (versioning, staging, production)                │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

| Component | Purpose | When You'll Learn It |
|-----------|---------|---------------------|
| **Tracking** | Log experiments — parameters, metrics, artifacts, code | Module 2 |
| **Projects** | Package ML code for reproducibility | Module 6 |
| **Models** | Standard format for saving/loading models across frameworks | Module 5 |
| **Model Registry** | Central model store with versioning & lifecycle management | Module 4 |

---

## 3. MLFlow Architecture

### Key Concepts

| Concept | Description | Example |
|---------|-------------|---------|
| **Experiment** | A named group of related runs | "wine-quality-classification" |
| **Run** | A single execution of ML code | One training with specific hyperparameters |
| **Parameter** | Input configuration value | `max_depth=5`, `learning_rate=0.01` |
| **Metric** | Output measurement | `accuracy=0.87`, `rmse=0.42` |
| **Artifact** | Output file | Model file, plot, dataset snapshot |
| **Tag** | Key-value metadata | `team=data-science`, `version=v2` |

### Backend Architecture

```
Your Code (Python)
    │
    ▼
MLFlow Client (Python API)
    │
    ├──▶ Backend Store (where metadata goes)
    │       • SQLite database (our default): sqlite:///mlflow.db
    │       • PostgreSQL / MySQL (production)
    │       • File store (legacy, deprecated): ./mlruns/
    │
    └──▶ Artifact Store (where files go)
            • Local filesystem (default): ./mlartifacts/
            • Remote: S3, GCS, Azure Blob Storage
```

> **💡 Key Insight**: In this course, we use a **SQLite database** (`mlflow.db`) at the project root to store all experiment metadata (params, metrics, tags). Artifacts (models, plots) are stored in the `mlartifacts/` folder. SQLite is a single-file database — no server needed, but it supports the Model Registry and fast SQL queries!

---

## 4. MLFlow vs Other Tools

| Feature | MLFlow | Weights & Biases | Neptune | DVC |
|---------|--------|-------------------|---------|-----|
| Open Source | ✅ | ❌ (freemium) | ❌ (freemium) | ✅ |
| Self-hosted | ✅ | ❌ | ❌ | ✅ |
| Experiment Tracking | ✅ | ✅ | ✅ | ✅ |
| Model Registry | ✅ | ✅ | ✅ | ❌ |
| Model Serving | ✅ | ❌ | ❌ | ❌ |
| Projects (Reproducibility) | ✅ | ❌ | ❌ | ✅ |
| Framework Agnostic | ✅ | ✅ | ✅ | ✅ |

**Why MLFlow?** It's the only tool that covers **all 4 pillars** (tracking, projects, models, registry) while being **fully open-source** and **self-hostable**.

---

## 🔑 Key Takeaways

1. **MLOps** brings software engineering discipline to ML — solving tracking, reproducibility, and deployment challenges
2. **MLFlow** has 4 components: Tracking, Projects, Models, and Model Registry
3. We use a **SQLite database** (`mlflow.db`) for structured, local storage — no server needed to start
4. MLFlow is **framework-agnostic** — works with scikit-learn, PyTorch, TensorFlow, and more
5. The **Tracking** component (Module 2) is the foundation — you'll use it in every project

---

## ➡️ Next Steps

Open `02_installation_setup.ipynb` to verify your installation, then `03_first_experiment.ipynb` for your first hands-on experiment!
