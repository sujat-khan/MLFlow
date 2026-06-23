# Module 6: MLFlow Projects

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand why **reproducibility** matters in ML
- Create an **MLproject** file with entry points and parameters
- Define **environments** (conda, virtualenv) for projects
- **Run projects** locally and from Git repositories

---

## 1. Why MLFlow Projects?

The problem: "It works on my laptop!"

ML code often breaks when someone else tries to run it because of:
- Different Python versions
- Missing or incompatible library versions
- Hardcoded paths
- Missing data or configuration

**MLFlow Projects** solve this by packaging code with its **environment** and **entry points**.

---

## 2. Project Structure

```
my_project/
├── MLproject           # Project definition (entry points, params)
├── conda.yaml          # Environment definition
├── train.py            # Training script (entry point)
└── evaluate.py         # Evaluation script (entry point)
```

### MLproject File

```yaml
name: wine-quality-project

conda_env: conda.yaml    # Or: python_env: python_env.yaml

entry_points:
  train:
    parameters:
      n_estimators: {type: int, default: 100}
      max_depth: {type: int, default: 5}
      data_path: {type: str, default: "data/wine.csv"}
    command: "python train.py --n_estimators {n_estimators} --max_depth {max_depth} --data_path {data_path}"
  
  evaluate:
    parameters:
      run_id: {type: str}
    command: "python evaluate.py --run_id {run_id}"
```

### Environment Specs

```yaml
# conda.yaml
name: wine-project-env
channels:
  - defaults
dependencies:
  - python=3.10
  - pip
  - pip:
    - mlflow>=2.15.0
    - scikit-learn>=1.5.0
    - pandas>=2.2.0
```

---

## 3. Running Projects

```python
# Run locally
mlflow.run(".", entry_point="train", parameters={"n_estimators": 200})

# Run from Git
mlflow.run(
    "https://github.com/user/repo.git",
    entry_point="train",
    parameters={"n_estimators": 200}
)
```

---

## Key Rules

> ⚠️ **Entry points must be `.py` scripts** (not notebooks). Notebooks can orchestrate project runs but can't be entry points themselves.

---

## ➡️ Next Steps
1. Examine the `sample_project/` directory
2. Work through `02_create_run_projects.ipynb`
3. Complete `03_exercises.ipynb`
