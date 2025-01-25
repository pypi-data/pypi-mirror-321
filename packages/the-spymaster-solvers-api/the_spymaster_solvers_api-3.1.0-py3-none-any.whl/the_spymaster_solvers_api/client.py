import logging
from typing import Optional

from the_spymaster_util.http.client import HTTPClient
from urllib3 import Retry

from .structs import (
    GenerateClueRequest,
    GenerateClueResponse,
    GenerateGuessRequest,
    GenerateGuessResponse,
    LoadModelsRequest,
    LoadModelsResponse,
)
from .structs.errors import SERVICE_ERRORS

log = logging.getLogger(__name__)
DEFAULT_BASE_URL = "http://localhost:5000"
DEFAULT_RETRY_STRATEGY = Retry(
    raise_on_status=False,
    total=5,
    backoff_factor=0.3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "OPTIONS", "GET", "POST", "PUT", "DELETE"],
)


class TheSpymasterSolversClient(HTTPClient):
    def __init__(self, base_url: str = DEFAULT_BASE_URL, retry_strategy: Optional[Retry] = DEFAULT_RETRY_STRATEGY):
        super().__init__(base_url=base_url, retry_strategy=retry_strategy, common_errors=SERVICE_ERRORS)

    def generate_clue(self, request: GenerateClueRequest) -> GenerateClueResponse:
        data = self.post(endpoint="generate-clue", data=request.model_dump())
        return GenerateClueResponse(**data)

    def generate_guess(self, request: GenerateGuessRequest) -> GenerateGuessResponse:
        data = self.post(endpoint="generate-guess", data=request.model_dump())
        return GenerateGuessResponse(**data)

    def load_models(self, request: LoadModelsRequest) -> LoadModelsResponse:
        data = self.post(endpoint="load-models", data=request.model_dump())
        return LoadModelsResponse(**data)
