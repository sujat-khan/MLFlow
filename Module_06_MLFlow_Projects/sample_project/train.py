"""
Wine Quality Training Script — MLFlow Project Entry Point

Usage:
    python train.py --n_estimators 100 --max_depth 5
"""
import argparse
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score


def parse_args():
    parser = argparse.ArgumentParser(description="Train a wine quality classifier")
    parser.add_argument("--n_estimators", type=int, default=100,
                        help="Number of trees in the forest")
    parser.add_argument("--max_depth", type=int, default=5,
                        help="Maximum depth of the trees")
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Load data
    wine = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(
        wine.data, wine.target, test_size=0.2, random_state=42
    )
    
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("n_estimators", args.n_estimators)
        mlflow.log_param("max_depth", args.max_depth)
        mlflow.log_param("model_type", "RandomForest")
        
        # Train model
        model = RandomForestClassifier(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            random_state=42
        )
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="weighted")
        
        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)
        
        # Log model with signature
        signature = infer_signature(X_train, y_pred)
        mlflow.sklearn.log_model(
            model, 
            artifact_path="model",
            signature=signature
        )
        
        print(f"Model trained: accuracy={accuracy:.4f}, f1={f1:.4f}")
        print(f"n_estimators={args.n_estimators}, max_depth={args.max_depth}")


if __name__ == "__main__":
    main()
