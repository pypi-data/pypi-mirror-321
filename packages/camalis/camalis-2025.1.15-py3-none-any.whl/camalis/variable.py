from datetime import datetime, UTC

from camalis.core import BaseCamalisClient
from camalis.exceptions import CamalisException, CamalisApiException
from camalis.utils import datetime_to_iso_string, iso_string_to_datetime


class Variable:
    _id = None
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient, id):
        self._id = id
        self._camalis = client

    def historic(self, start_time: datetime, end_time: datetime):
        start = datetime_to_iso_string(start_time)
        end = datetime_to_iso_string(end_time)
        response = self._camalis.request_get(
            f'/variaveis/historico/?variavelId={self._id}&dataInicio={start}&dataFim={end}')

        if not response['status']:
            return response['detalhes']
        result = []
        for data in response['dados']:
            result.append({
                'timestamp': iso_string_to_datetime(data['t']),
                'value': data['v'],
                'unit': data['u']
            })
        return result

    def statistics(self, start_time: datetime, end_time: datetime, interval_in_seconds=3600):
        response = self._camalis.request_post('/variaveis/historico/', {
            "dataInicio": datetime_to_iso_string(start_time),
            "dataFim": datetime_to_iso_string(end_time),
            "variavelId": self._id,
            "intervaloEmSegundos": interval_in_seconds
        })
        return response['statistics']

    def __str__(self):
        return f"Variable {self._id}"

    @property
    def id(self):
        return self._id

    def snapshot(self):
        response = self._camalis.request_get(f'/variaveis/snapshot/?variavelId={self._id}')
        if not response['status']:
            raise CamalisException(response['detalhes'])

        if response['dados'] is None:
            return None

        return {
            'timestamp': iso_string_to_datetime(response['dados']['t']),
            'value': response['dados']['v'],
            'unit': response['dados']['u']
        }

    def write(self, value, created_at: datetime = None):
        start = datetime_to_iso_string(created_at) if created_at else datetime_to_iso_string(datetime.now(tz=UTC))
        self._camalis.request_post('/variaveis/escrever/', {
            "variavel_id": self._id,
            "datahora": start,
            "valor": value
        })
        return True


class CamalisVariableClient:
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient):
        self._camalis = client

    def get(self, name=None, path=None) -> Variable:
        """
        Get variable by name or path
        :param name: name of the variable
        :param path: path of the variable
        :return: Variable object
        :raises CamalisApiException: if variable not found
        :raises CamalisApiException: if multiple variables found
        :raises CamalisApiException: if name or path is not provided
        """
        if path is None and name is None:
            raise CamalisApiException('Name or path is required')

        if path and name:
            raise CamalisApiException('Only one parameter is allowed')

        response = None

        url = '/variaveis/'
        if name:
            if self._camalis.element_id is None:
                raise CamalisApiException('ElementId is required')

            url = f'{url}buscarPorNome/?nome={name}&elementoId={self._camalis.element_id}'
            response = self._camalis.request_get(url=url)

        if path:
            url = f'{url}buscarPorPath/?path={path}'
            response = self._camalis.request_get(url=url)

        if len(response['ids']) == 0:
            raise CamalisApiException('Variable not found')

        if len(response['ids']) > 1:
            raise CamalisApiException('Multiple variables found, if you want to list use list method')

        return Variable(self._camalis, id=response['ids'][0])

    def list(self, path=None) -> list[Variable]:
        """
        List variables by path
        :param path: path of the variables
        :return: list of Variable objects
        """
        if path is None and self._camalis.element_id is None:
            raise CamalisApiException('Path or element_id is required')

        url = f'/variaveis/buscarPorPath/?path={path}' \
            if path else f'/variaveis/buscarPorNome/?nome=&elementoId={self._camalis.element_id}'
        response = self._camalis.request_get(url=url)
        if len(response['ids']) == 0:
            return []

        result = []
        for variable_id in response['ids']:
            result.append(Variable(self._camalis, id=variable_id))
        return result
