from pydantic_settings import BaseSettings
from gcp_secrets import GCPSecrets
import base64

secrets = GCPSecrets()


class AppConfig(BaseSettings):
    MLFLOW_TRACKING_USERNAME: str = secrets.get_secret("mlflow_server_username")
    MLFLOW_TRACKING_PASSWORD: str = secrets.get_secret("mlflow_server_password")
    KSERVE_ENDPOINT: str = secrets.get_secret("kserve_internal_endpoint")
    MODEL_NAME: str = "your-kserve-model-name"


def get_config() -> AppConfig:
    return AppConfig()


app_config = get_config()
