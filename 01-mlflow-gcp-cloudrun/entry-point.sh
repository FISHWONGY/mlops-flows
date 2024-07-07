#!/usr/bin/env bash

set -e

export PYTHONPATH="${PYTHONPATH}:/usr/src/app"

if [[ -z "${GCP_PROJECT}" ]]; then
    echo "Error: GCP_PROJECT not set"
    exit 1
fi

export MLFLOW_TRACKING_USERNAME="$(poetry run python ./get_secret.py --project="${GCP_PROJECT}" --secret=mlflow_server_username)"
export MLFLOW_TRACKING_PASSWORD="$(poetry run python ./get_secret.py --project="${GCP_PROJECT}" --secret=mlflow_server_password)"
export ARTIFACT_URL="$(poetry run python ./get_secret.py --project="${GCP_PROJECT}" --secret=mlflow_artifact_url)"
if [[ -z "${DATABASE_URL}" ]]; then
    export DATABASE_URL="$(poetry run python ./get_secret.py --project="${GCP_PROJECT}" --secret=mlflow_database_url)"
fi

if [[ -z "${MLFLOW_TRACKING_USERNAME}" ]]; then
    echo "Error: MLFLOW_TRACKING_USERNAME not set"
    exit 1
fi

if [[ -z "${MLFLOW_TRACKING_PASSWORD}" ]]; then
    echo "Error: MLFLOW_TRACKING_PASSWORD not set"
    exit 1
fi

if [[ -z "${ARTIFACT_URL}" ]]; then
    echo "Error: ARTIFACT_URL not set"
    exit 1
fi

if [[ -z "${DATABASE_URL}" ]]; then
    echo "Error: DATABASE_URL not set"
    exit 1
fi

if [[ -z "${PORT}" ]]; then
    export PORT=8080
fi

if [[ -z "${HOST}" ]]; then
    export HOST=0.0.0.0
fi

export WSGI_AUTH_CREDENTIALS="${MLFLOW_TRACKING_USERNAME}:${MLFLOW_TRACKING_PASSWORD}"
export _MLFLOW_SERVER_ARTIFACT_ROOT="${ARTIFACT_URL}"
export _MLFLOW_SERVER_FILE_STORE="${DATABASE_URL}"

exec poetry run gunicorn -b "${HOST}:${PORT}" -w 4 --log-level debug --access-logfile=- --error-logfile=- mlflow_auth:app
