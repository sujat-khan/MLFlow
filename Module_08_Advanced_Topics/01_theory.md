# Module 8: Advanced Topics

## 🎯 Learning Objectives

By the end of this module, you will:
- Integrate **Optuna** with MLFlow for hyperparameter optimization
- Track **complete ML pipelines** with stage-based tagging
- Configure **PostgreSQL** as a production backend store
- Set up a **remote MLFlow tracking server**

---

## 1. Hyperparameter Optimization with Optuna

**Optuna** is a next-gen HPO framework that supports:
- Bayesian optimization (Tree-structured Parzen Estimator)
- Pruning (stop bad trials early)
- Native MLFlow integration

```python
import optuna

def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 50, 300)
    max_depth = trial.suggest_int("max_depth", 2, 20)
    # ... train and evaluate
    return accuracy

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50)
```

---

## 2. Pipeline Tracking

Track multi-stage ML pipelines by linking stages with tags:

```
Stage 1: Data Preprocessing → Run (tagged: stage=preprocess)
Stage 2: Feature Engineering → Run (tagged: stage=features)  
Stage 3: Model Training     → Run (tagged: stage=train)
Stage 4: Evaluation         → Run (tagged: stage=evaluate)
```

---

## 3. Database Backends

| Backend | URI Format | Best For |
|---------|------------|----------|
| File Store | `./mlruns` | Development |
| SQLite | `sqlite:///mlflow.db` | Single user |
| PostgreSQL | `postgresql://user:pass@host:5432/db` | Production |

---

## ➡️ Next Steps

1. `02_hyperparameter_tuning.ipynb` — Optuna + MLFlow
2. `03_pipeline_tracking.ipynb` — Pipeline tracking
3. `04_database_backends.ipynb` — PostgreSQL setup
4. `05_remote_tracking_server.md` — Remote server guide
