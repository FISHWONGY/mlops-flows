from pydantic_settings import BaseSettings

from gcp_secrets import GCPSecrets

secrets = GCPSecrets()


class AppConfig(BaseSettings):
    MLFLOW_TRACKING_USERNAME: str = secrets.get_secret("mlflow_server_username")
    MLFLOW_TRACKING_PASSWORD: str = secrets.get_secret("mlflow_server_password")

    GCP_CREDS: str = secrets.get_secret("svc-creds-json")

    PROJECT_ID: str = "gcp-prj-id-123"
    REGION: str = "us-central1"
    ENDPOINT_ID: str = "1234567"
    ENDPOINT_URL: str = f"https://{REGION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/endpoints/{ENDPOINT_ID}:predict"


def get_config() -> AppConfig:
    return AppConfig()


app_config = get_config()
