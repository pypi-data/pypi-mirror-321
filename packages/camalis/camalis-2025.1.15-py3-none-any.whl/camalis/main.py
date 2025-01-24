import os

from camalis.core import BaseCamalisClient
from camalis.dataset import CamalisDatasetClient
from camalis.element import CamalisElementClient
from camalis.event import CamalisEventClient
from camalis.exceptions import CamalisAuthException
from camalis.model import CamalisModelClient
from camalis.variable import CamalisVariableClient


class Camalis(BaseCamalisClient):
    """
    Camalis client
    """
    variable: CamalisVariableClient = None
    event: CamalisEventClient = None

    def __init__(self, api_url=None, token=None, element_id=None):
        """
        Initialize Camalis client
        :param api_url: URL of the Camalis API
        :param token: Token for the Camalis API
        :param element_id: Element ID for the Camalis API
        """
        request_token = os.environ.get('CAMALIS_TOKEN', token)
        camalis_url = os.environ.get('CAMALIS_API_URL', api_url)
        camalis_element_id = os.environ.get('CAMALIS_ELEMENTO_ID', element_id)

        if request_token is None:
            raise CamalisAuthException('Token is required')

        if camalis_url is None:
            raise CamalisAuthException('API URL is required')

        super().__init__(camalis_url, request_token, camalis_element_id)
        self.variable = CamalisVariableClient(self)
        self.dataset = CamalisDatasetClient(self)
        self.model = CamalisModelClient(self)
        self.event = CamalisEventClient(self)
        self.element = CamalisElementClient(self)