# Module 5: MLFlow Models & Signatures

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand MLFlow **model flavors** and the MLmodel file format
- Create and enforce **model signatures** (input/output schemas)
- Build **custom PyFunc models** for complex inference logic
- Use **`mlflow.evaluate()`** for systematic model evaluation

---

## 1. Model Flavors

MLFlow uses **flavors** to support multiple ML frameworks with a unified API.

| Flavor | Framework | Import |
|--------|-----------|--------|
| `mlflow.sklearn` | scikit-learn | `mlflow.sklearn.log_model()` |
| `mlflow.pytorch` | PyTorch | `mlflow.pytorch.log_model()` |
| `mlflow.tensorflow` | TensorFlow/Keras | `mlflow.tensorflow.log_model()` |
| `mlflow.xgboost` | XGBoost | `mlflow.xgboost.log_model()` |
| `mlflow.pyfunc` | Any (generic) | `mlflow.pyfunc.log_model()` |

The **`pyfunc`** flavor is special — it provides a **universal interface** that works with any Python code. Every other flavor also creates a pyfunc-compatible interface.

---

## 2. The MLmodel File

When you log a model, MLFlow creates an `MLmodel` YAML file that describes:

```yaml
artifact_path: model
flavors:
  python_function:
    env: conda.yaml
    loader_module: mlflow.sklearn
    model_path: model.pkl
    python_version: 3.10.0
  sklearn:
    code: null
    pickled_model: model.pkl
    serialization_format: cloudpickle
    sklearn_version: 1.5.0
signature:
  inputs: '[{"name": "feature_1", "type": "double"}, ...]'
  outputs: '[{"type": "long"}]'
```

---

## 3. Model Signatures

A **signature** defines the expected input and output schema for a model:
- **Column-based** (tabular): named columns with types (most common)
- **Tensor-based**: numpy array shapes and dtypes

Signatures enable:
- ✅ Input validation (catch bad data before inference)
- ✅ Documentation (what does this model expect?)
- ✅ UI display (shown in MLFlow UI)

---

## 4. Custom PyFunc Models

When you need to add **preprocessing**, **postprocessing**, or **ensemble logic** that isn't a standard model, use a custom PyFunc model:

```python
class MyModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # Load any artifacts you need
        pass
    
    def predict(self, context, model_input, params=None):
        # Your custom prediction logic
        return predictions
```

---

## ➡️ Next Steps

1. `02_model_signature.ipynb` — Create and enforce signatures
2. `03_custom_pyfunc_models.ipynb` — Build custom PyFunc models
3. `04_model_evaluation.ipynb` — Use mlflow.evaluate()
4. `05_exercises.ipynb` — Practice
