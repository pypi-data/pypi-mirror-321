from datetime import datetime, UTC

from camalis.core import BaseCamalisClient
from camalis.exceptions import CamalisApiException, CamalisException
from camalis.utils import datetime_to_iso_string, iso_string_to_datetime


class Event:
    _name: str = None
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient, name: str):
        self._camalis = client
        self._name = name

    @property
    def name(self):
        return self._name

    def snapshot(self):
        response = self._camalis.request_get(
            f'/eventos/snapshot/?elementoId={self._camalis.element_id}&evento={self._name}')
        if not response['status']:
            raise CamalisException(response['detalhes'])

        if response['dados'] is None:
            return None

        return {
            'timestamp': iso_string_to_datetime(response['dados']['t']),
            'value': response['dados']['v'],
        }

    def historic(self, start_time: datetime, end_time: datetime):
        start = datetime_to_iso_string(start_time)
        end = datetime_to_iso_string(end_time)
        response = self._camalis.request_get(
            f'/eventos/historico/?elementoId={self._camalis.element_id}&dataInicio={start}&dataFim={end}&evento={self._name}')

        if not response['status']:
            return response['detalhes']

        result = []
        for data in response['dados']:
            result.append({
                'timestamp': iso_string_to_datetime(data['t']),
                'value': data['v'],
            })
        return result

    def dispatch(self, created_at: datetime = None):
        start = datetime_to_iso_string(created_at) if created_at else datetime_to_iso_string(datetime.now(tz=UTC))
        self._camalis.request_post('/eventos/disparar/', {
            "elemento_id": self._camalis.element_id,
            "valor": self._name,
            "datahora": start,
        })
        return True


class CamalisEventClient:
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient):
        self._camalis = client

    def get(self, event_name) -> Event:
        if event_name is None:
            raise CamalisApiException('Event name is required')

        return Event(self._camalis, name=event_name)
