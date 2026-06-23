# Module 3: Experiments & the MLFlow UI

## 🎯 Learning Objectives

By the end of this module, you will:
- Create, manage, and organize **experiments** effectively
- **Search and filter** runs programmatically with powerful query syntax
- Master the **MLFlow UI** for visual experiment analysis
- Understand experiment lifecycle (active, deleted, restored)

---

## 1. What is an Experiment?

An **experiment** is a named container that groups related runs. Think of it as a project or research question.

```
MLFlow Server
├── Experiment: "wine-quality-classification"
│   ├── Run: random_forest_v1
│   ├── Run: random_forest_v2
│   └── Run: gradient_boosting_v1
│
├── Experiment: "customer-churn-prediction"
│   ├── Run: baseline_logreg
│   └── Run: xgboost_tuned
│
└── Experiment: "Default" (id=0)
    └── Runs not assigned to any experiment
```

### Naming Best Practices

| Pattern | Example | When to Use |
|---------|---------|-------------|
| `project-task` | `wine-quality-classification` | Clear project scope |
| `team/project` | `ml-eng/fraud-detection` | Multi-team environments |
| `project-phase` | `churn-v2-feature-engineering` | Iterative development |

---

## 2. Experiment API

```python
# Create experiment
exp_id = mlflow.create_experiment("my_experiment", tags={"team": "ml"})

# Set active experiment (creates if doesn't exist)
mlflow.set_experiment("my_experiment")

# Get experiment by name
exp = mlflow.get_experiment_by_name("my_experiment")

# Get experiment by ID
exp = mlflow.get_experiment(exp_id)

# List all experiments
experiments = mlflow.search_experiments()

# Delete experiment (soft delete — can be restored)
mlflow.delete_experiment(exp_id)
```

---

## 3. Searching Runs

The `mlflow.search_runs()` function is incredibly powerful:

```python
# Basic search
runs = mlflow.search_runs(experiment_names=["my_experiment"])

# Filter by metric
runs = mlflow.search_runs(
    experiment_names=["my_experiment"],
    filter_string="metrics.accuracy > 0.9"
)

# Filter by parameter
runs = mlflow.search_runs(
    filter_string="params.model_type = 'RandomForest'"
)

# Filter by tag
runs = mlflow.search_runs(
    filter_string="tags.purpose = 'baseline'"
)

# Combine filters with AND
runs = mlflow.search_runs(
    filter_string="metrics.accuracy > 0.85 AND params.model_type = 'RandomForest'"
)

# Sort results
runs = mlflow.search_runs(
    order_by=["metrics.accuracy DESC"]
)
```

### Filter Syntax Reference

| Operator | Example | Description |
|----------|---------|-------------|
| `=` | `params.model = 'RF'` | Exact match |
| `!=` | `params.model != 'RF'` | Not equal |
| `>`, `>=` | `metrics.acc > 0.9` | Greater than |
| `<`, `<=` | `metrics.loss < 0.5` | Less than |
| `LIKE` | `params.model LIKE 'Random%'` | Pattern match |
| `AND` | `metrics.acc > 0.9 AND params.model = 'RF'` | Combine filters |

---

## 4. The MLFlow UI

The UI at `http://localhost:5000` provides:

| Feature | What It Does |
|---------|--------------|
| **Experiments List** | Browse all experiments in the sidebar |
| **Runs Table** | See all runs with sortable columns |
| **Compare Runs** | Select 2+ runs and view side-by-side comparison |
| **Charts** | Visualize metrics across runs (bar, scatter, line) |
| **Artifact Browser** | View logged files (plots, models, data) |
| **Run Details** | Click a run to see all params, metrics, tags, artifacts |

---

## ➡️ Next Steps

1. `02_create_manage_experiments.ipynb` — Hands-on experiment management
2. `03_search_filter_runs.ipynb` — Powerful search & filtering
3. `04_mlflow_ui_guide.md` — Visual UI walkthrough
4. `05_exercises.ipynb` — Practice problems
