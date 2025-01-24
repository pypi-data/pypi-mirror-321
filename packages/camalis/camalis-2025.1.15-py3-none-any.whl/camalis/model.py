from camalis.core import BaseCamalisClient
from camalis.exceptions import CamalisApiException


class CamalisModelClient:
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient):
        self._camalis = client

    def download(self, modelo_id):
        """
        Get model by id
        :param modelo_id: ID of the model to download
        :return: loaded model
        """

        if modelo_id is None:
            raise CamalisApiException('Model ID is required')

        url = 'modelo'
        response = self._camalis.request_get(f'/{url}/download/{modelo_id}')

        return response