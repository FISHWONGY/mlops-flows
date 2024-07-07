import mlflow.pyfunc
import os
from settings import app_config

os.environ["MLFLOW_TRACKING_USERNAME"] = app_config.MLFLOW_TRACKING_USERNAME
os.environ["MLFLOW_TRACKING_PASSWORD"] = app_config.MLFLOW_TRACKING_PASSWORD
os.environ["MLFLOW_TRACKING_URI"] = app_config.MLFLOW_TRACKING_URI


def load_latest_model():
    model = mlflow.pyfunc.load_model(f"models:/{app_config.MODEL_NAME}@Production")
    return model
