from fastapi import Depends, FastAPI, Response, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasicCredentials

from typing import List, Annotated
import pandas as pd

from helpers.models import WineQualityInput
from helpers.load_mlflow_models import load_latest_model
from basic_auth import validate

from os import getenv
import google.cloud.logging
import logging


if (env := getenv("ENV")) and env == "prod":
    client = google.cloud.logging.Client()
    client.setup_logging()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/health")
async def health():
    return "ok"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logger.error(f"{request}: {exc_str}")
    content = {"code": 422, "message": exc_str, "data": None}
    return JSONResponse(content=content, status_code=422)


@app.post("/invocations")
async def invocations(
    inputs: List[WineQualityInput],
    credentials: Annotated[HTTPBasicCredentials, Depends(validate)],
):
    input_df = pd.DataFrame([input_data.dict() for input_data in inputs])

    model = load_latest_model()

    try:
        predictions = model.predict(input_df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return predictions.tolist()


# @app.post("/invocations")
# async def invocations(
#     inputs: List[WineQualityInput],
# ):
#     input_df = pd.DataFrame([input_data.dict() for input_data in inputs])
#
#     model = load_latest_model()
#
#     try:
#         predictions = model.predict(input_df)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
#     return predictions.tolist()
