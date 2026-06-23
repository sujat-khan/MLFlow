# Module 4: Model Registry

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand the **Model Registry** concepts: registered models, versions, aliases
- **Register models** from runs into the registry
- Manage **model versions** and compare them
- Implement **Champion/Challenger** workflows using aliases
- Use the registry for **production model management**

---

## 1. Why a Model Registry?

Without a registry:
```
😩 "Which model is running in production?"
😩 "Who approved the latest model update?"
😩 "Can we roll back to the previous model version?"
```

The Model Registry solves this by providing a **central store** for model lifecycle management.

---

## 2. Key Concepts

```
Model Registry
├── Registered Model: "wine-quality-classifier"
│   ├── Version 1 (source: run abc123)
│   │   └── Alias: none
│   ├── Version 2 (source: run def456)
│   │   └── Alias: "challenger"
│   └── Version 3 (source: run ghi789)
│       └── Alias: "champion"  ← Currently in production
│
└── Registered Model: "customer-churn-model"
    ├── Version 1
    └── Version 2
```

| Concept | Description |
|---------|-------------|
| **Registered Model** | A named model (e.g., "wine-quality-classifier") |
| **Model Version** | A specific trained instance (linked to a run) |
| **Alias** | A named pointer to a version (e.g., "champion", "challenger") |
| **Description** | Human-readable notes about the model or version |
| **Tags** | Key-value metadata for organization |

### Aliases (replacing Stages)

> ⚠️ **Note**: MLFlow previously used "Stages" (None → Staging → Production → Archived). This has been **deprecated** in favor of **Aliases**, which are more flexible.

| Alias | Purpose |
|-------|---------|
| `champion` | The current production model |
| `challenger` | A candidate model being evaluated |
| `baseline` | The reference model for comparison |

---

## 3. Registration Methods

```python
# Method 1: Register during logging (in a run)
mlflow.sklearn.log_model(
    model, 
    artifact_path="model",
    registered_model_name="wine-quality-classifier"  # ← This registers it!
)

# Method 2: Register after the fact
mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="wine-quality-classifier"
)
```

---

## 4. Loading Models from Registry

```python
# Load latest version
model = mlflow.sklearn.load_model("models:/wine-quality-classifier/latest")

# Load specific version
model = mlflow.sklearn.load_model("models:/wine-quality-classifier/3")

# Load by alias (RECOMMENDED for production)
model = mlflow.sklearn.load_model("models:/wine-quality-classifier@champion")
```

---

## ➡️ Next Steps

1. `02_register_models.ipynb` — Register models hands-on
2. `03_model_versions.ipynb` — Manage versions
3. `04_stage_transitions.ipynb` — Champion/Challenger workflow
4. `05_exercises.ipynb` — Practice
