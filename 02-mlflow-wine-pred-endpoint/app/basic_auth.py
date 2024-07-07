import secrets
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from settings import app_config

security = HTTPBasic()

AUTH_USERNAME = app_config.MLFLOW_TRACKING_USERNAME.encode("utf8")
AUTH_PASSWORD = app_config.MLFLOW_TRACKING_PASSWORD.encode("utf8")


def validate(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    current_username_bytes = credentials.username.encode("utf8")
    is_correct_username = secrets.compare_digest(current_username_bytes, AUTH_USERNAME)
    current_password_bytes = credentials.password.encode("utf8")
    is_correct_password = secrets.compare_digest(current_password_bytes, AUTH_PASSWORD)
    if not (is_correct_username and is_correct_password):
        raise HTTPException(status_code=401)
    return credentials.username
