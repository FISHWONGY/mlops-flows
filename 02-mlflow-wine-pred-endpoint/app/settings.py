from pydantic_settings import BaseSettings
from gcp_secrets import GCPSecrets

secrets = GCPSecrets()


class AppConfig(BaseSettings):
    MLFLOW_TRACKING_USERNAME: str = secrets.get_secret("mlflow_server_username")
    MLFLOW_TRACKING_PASSWORD: str = secrets.get_secret("mlflow_server_password")
    MLFLOW_TRACKING_URI: str = secrets.get_secret("mlflow_tracking_uri")
    MODEL_NAME: str = "wine_quality"


def get_config() -> AppConfig:
    return AppConfig()


app_config = get_config()
