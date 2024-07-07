from pydantic_settings import BaseSettings
from gcp_secrets import GCPSecrets
import base64

secrets = GCPSecrets()


class AppConfig(BaseSettings):
    MLFLOW_TRACKING_USERNAME: str = secrets.get_secret("mlflow_server_username")
    MLFLOW_TRACKING_PASSWORD: str = secrets.get_secret("mlflow_server_password")
    MLFLOW_TRACKING_URI: str = secrets.get_secret("mlflow_tracking_uri")
    CRED_STR: str = f"{MLFLOW_TRACKING_USERNAME}:{MLFLOW_TRACKING_PASSWORD}"
    CRED_BYTES: bytes = str.encode(CRED_STR)
    CREDENTIALS: str = base64.b64encode(CRED_BYTES).decode("utf-8")


def get_config() -> AppConfig:
    return AppConfig()


app_config = get_config()
