# Module 2: MLFlow Tracking — Deep Dive

## 🎯 Learning Objectives

By the end of this module, you will:
- Master all **Tracking API methods** (params, metrics, artifacts, tags)
- Understand **step-based metric logging** for training curves
- Use **autolog** to automatically capture everything
- Organize complex experiments with **nested runs**
- Know the difference between **backend store** and **artifact store**

---

## 1. Tracking Architecture

MLFlow Tracking is the most-used component. It lets you log and query experiments using a simple API.

### What Gets Stored Where

```
mlflow.start_run()
    │
    ├── Parameters ──────▶ Backend Store (SQLite)
    │   (input config)       • Database: params table
    │
    ├── Metrics ─────────▶ Backend Store (SQLite)
    │   (output values)      • Database: metrics table
    │
    ├── Tags ────────────▶ Backend Store (SQLite)
    │   (metadata)           • Database: tags table
    │
    └── Artifacts ───────▶ Artifact Store
        (files)              • Local: mlartifacts/<exp_id>/<run_id>/artifacts/
                             • Remote: S3, GCS, Azure Blob
```

### Key Differences

| | Parameters | Metrics | Tags | Artifacts |
|---|---|---|---|---|
| **Type** | String key-value | Numeric key-value | String key-value | Files |
| **Purpose** | Input configuration | Output measurements | Metadata labels | Output files |
| **Mutable?** | ❌ Immutable once logged | ✅ Can log same key multiple times (steps) | ✅ Can overwrite | ❌ Append only |
| **Searchable?** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Example** | `learning_rate=0.01` | `accuracy=0.95` | `team=ml-eng` | `model.pkl`, `plot.png` |

---

## 2. The Tracking API at a Glance

```python
# Parameters (inputs)
mlflow.log_param("key", value)        # Single parameter
mlflow.log_params({"k1": v1, "k2": v2})  # Multiple parameters

# Metrics (outputs)
mlflow.log_metric("key", value)       # Single metric
mlflow.log_metric("loss", 0.5, step=1)  # With step (for training curves)
mlflow.log_metrics({"k1": v1, "k2": v2})  # Multiple metrics

# Tags (metadata)
mlflow.set_tag("key", "value")        # Single tag
mlflow.set_tags({"k1": "v1", "k2": "v2"})  # Multiple tags

# Artifacts (files)
mlflow.log_artifact("path/to/file")   # Single file
mlflow.log_artifacts("path/to/dir")   # Entire directory
```

---

## 3. Autolog — The Easy Way

Instead of manually logging everything, MLFlow can **automatically** capture parameters, metrics, and models:

```python
# Auto-log for all supported frameworks
mlflow.autolog()

# Or framework-specific
mlflow.sklearn.autolog()
mlflow.pytorch.autolog()
mlflow.tensorflow.autolog()
```

### What Autolog Captures (scikit-learn)

| Logged Automatically | Example |
|---------------------|---------|
| All constructor parameters | `max_depth=5`, `n_estimators=100` |
| Training metrics | `training_accuracy`, `training_f1_score` |
| The trained model | Saved as artifact with signature |
| Model signature | Input/output schema |
| Input example | First few rows of training data |

---

## 4. Nested Runs

For complex experiments (like hyperparameter sweeps), you can create **parent-child** run hierarchies:

```
Parent Run: "HPO Sweep"
    ├── Child Run: trial_1 (lr=0.01, depth=3)
    ├── Child Run: trial_2 (lr=0.05, depth=5)
    └── Child Run: trial_3 (lr=0.1, depth=7)
```

This keeps the UI organized and shows relationships between runs.

---

## 🔑 Key Takeaways

1. **Parameters** are immutable inputs; **Metrics** are mutable outputs that support steps
2. **Tags** are for metadata/organization; **Artifacts** are for files (models, plots, data)
3. **Autolog** is the fastest way to start — it captures everything automatically
4. **Nested runs** help organize complex experiments like hyperparameter sweeps
5. The backend store holds metadata (params/metrics/tags); the artifact store holds files

---

## ➡️ Next Steps

Work through the notebooks in order:
1. `02_logging_basics.ipynb` — Parameters, metrics, tags
2. `03_logging_artifacts.ipynb` — Files, plots, datasets
3. `04_auto_logging.ipynb` — Autolog with scikit-learn
4. `05_nested_runs.ipynb` — Parent-child run relationships
5. `06_exercises.ipynb` — Practice problems
