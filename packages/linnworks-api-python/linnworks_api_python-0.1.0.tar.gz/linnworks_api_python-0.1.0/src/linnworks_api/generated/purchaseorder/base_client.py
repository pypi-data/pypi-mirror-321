from functools import cached_property
from typing import Optional, Dict, Any
from .api_client import ApiClient  # type: ignore will be relative imports when copied into each generated client
from .configuration import Configuration  # type: ignore will be relative imports when copied into each generated client
from linnworks_api.generated.auth.api import AuthApi
from linnworks_api.generated.auth.models.authorize_by_application_request import AuthorizeByApplicationRequest
import logging
import os

logging.basicConfig(level=os.getenv("LOG_LEVEL", logging.INFO))
logger = logging.getLogger(__name__)


class LinnworksConfig:
    def __init__(
        self,
        client_id,
        client_secret,
        token=None,
    ):
        """
        LinnworksConfig is a configuration object for the Linnworks API client.
        :param client_id: The client ID for the Linnworks API client.
        :param client_secret: The client secret for the Linnworks API client.
        :param token: The refresh token for the Linnworks API client.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token


class LinnworksClient(ApiClient):
    def __init__(self, linnworks_config: LinnworksConfig, config: Configuration = None):
        config = config or Configuration()
        super().__init__(configuration=config)
        self.linnworks_config = linnworks_config

    @cached_property
    def token(self) -> str:
        logger.info(f"Getting token for {self.linnworks_config.client_id}")
        props = AuthorizeByApplicationRequest(
            ApplicationId=self.linnworks_config.client_id,
            ApplicationSecret=self.linnworks_config.client_secret,
            Token=self.linnworks_config.token,
        )
        response = AuthApi().authorize_by_application(props)
        assert response.token is not None
        logger.info(f"Token for {self.linnworks_config.client_id} received")
        return response.token

    def call_api(
        self,
        method: str,
        url: str,
        header_params: Optional[Dict[str, Any]] = None,
        body: Optional[Any] = None,
        post_params: Optional[Dict[str, Any]] = None,
        _request_timeout: Optional[int] = None,
    ):
        header_params = header_params or {}
        header_params["Authorization"] = self.token
        logger.debug(f"Token added to header for {self.linnworks_config.client_id}")
        return super().call_api(method, url, header_params, body, post_params, _request_timeout)
