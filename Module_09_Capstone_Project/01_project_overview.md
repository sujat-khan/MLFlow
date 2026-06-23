# Module 9: Capstone — End-to-End ML Project 🎓

## Project: Wine Quality Classification

Build a complete, production-grade ML workflow using **everything** you've learned in Modules 1–8.

---

## 🎯 Project Goals

1. **Data Preparation** — Load, explore, and prepare the Wine Quality dataset
2. **Experiment Tracking** — Train multiple models with full MLFlow tracking
3. **Model Comparison** — Programmatically compare and select the best model
4. **Model Registry** — Register, version, and manage model lifecycle
5. **Deployment** — Containerize and serve the champion model
6. **Documentation** — Maintain clear experiment notes and artifacts

---

## 📋 Requirements Checklist

### Data & Experiments
- [ ] Load Wine Quality dataset from sklearn
- [ ] Create a dedicated experiment: `"capstone-wine-quality"`
- [ ] Perform EDA with visualizations logged as artifacts
- [ ] Log dataset summary (shape, classes, feature stats)

### Model Training
- [ ] Train at least **4 different model types**
- [ ] Use **autolog** for at least one model
- [ ] Use **nested runs** for hyperparameter tuning on your best model type
- [ ] Log parameters, metrics, artifacts, and models for every run

### Model Selection
- [ ] Use `mlflow.search_runs()` to compare all models
- [ ] Build a comparison table/visualization
- [ ] Select the best model programmatically (by accuracy or F1)

### Model Registry
- [ ] Register the best model as `"wine-quality-capstone"`
- [ ] Add model description and tags
- [ ] Set the `champion` alias on the best version
- [ ] Register the second-best as a `challenger`

### Deployment
- [ ] Serve the champion model locally via `mlflow models serve`
- [ ] Send test predictions via REST API
- [ ] (Bonus) Build a Docker image of the model

### Code Quality
- [ ] All notebooks have markdown explanations
- [ ] Runs are named clearly
- [ ] Tags include author and purpose

---

## 📂 Notebook Sequence

| # | Notebook | Description |
|---|----------|-------------|
| 1 | `02_data_preparation.ipynb` | Load data, EDA, feature engineering |
| 2 | `03_experiment_training.ipynb` | Train 4+ model types with tracking |
| 3 | `04_model_comparison.ipynb` | Compare runs, visualize results |
| 4 | `05_registry_workflow.ipynb` | Register, version, champion/challenger |
| 5 | `06_deploy_and_predict.ipynb` | Serve and send predictions |

---

## 🏆 Success Criteria

When complete, you should be able to:
1. Open the MLFlow UI and see a well-organized experiment with named runs
2. Query your best model programmatically
3. Load the champion model by alias and make predictions
4. Explain every step of the ML lifecycle managed by MLFlow

---

## ➡️ Start with `02_data_preparation.ipynb`!
