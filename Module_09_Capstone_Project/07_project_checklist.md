# 📝 Capstone Project Checklist

Use this checklist to track your progress through the capstone project.

---

## Data & Experiments

- [ ] Load Wine Quality dataset from sklearn
- [ ] Create experiment: `"capstone-wine-quality"`
- [ ] Perform EDA with at least 2 visualizations logged as artifacts
- [ ] Log dataset summary (shape, classes, feature stats)

## Model Training

- [ ] Train at least **4 different model types** (DT, RF, GB, LR, SVM)
- [ ] Log parameters, metrics, artifacts, and models for every run
- [ ] Use **nested runs** for hyperparameter tuning (Optuna, 30+ trials)
- [ ] Train a **final model** with the best HPO parameters

## Model Selection

- [ ] Use `mlflow.search_runs()` to compare all models
- [ ] Build a comparison visualization (bar chart)
- [ ] Select best model programmatically by accuracy

## Model Registry

- [ ] Register the best model as `"wine-quality-capstone"`
- [ ] Add model description and tags
- [ ] Set `champion` alias on the best version
- [ ] Register and set `challenger` alias on second-best

## Deployment

- [ ] Load champion model by alias: `models:/wine-quality-capstone@champion`
- [ ] Serve the champion model via `mlflow models serve`
- [ ] Send test predictions via REST API using `requests`
- [ ] (Bonus) Build Docker image

## Code Quality

- [ ] All notebooks have markdown section headers
- [ ] All runs have descriptive names
- [ ] All runs have tags: `author`, `stage`, `model_type`

---

## 🏆 When Complete

You should be able to answer:

1. **"Which model is in production?"** → Load by alias `@champion`
2. **"How was it trained?"** → Link to source run in MLFlow UI
3. **"Can we reproduce it?"** → Parameters, data split, random seed all logged
4. **"How does it compare?"** → Comparison chart in MLFlow artifacts
5. **"How do I deploy it?"** → `mlflow models serve` or Docker

---

**Congratulations on completing the MLFlow course! 🎉**
