from typing import List

from camalis.core import BaseCamalisClient
from camalis.exceptions import CamalisApiException

class Element:
    _id = None
    _camalis: BaseCamalisClient = None
    _name = None
    _children = None
    _path = None

    def __init__(self, client: BaseCamalisClient, id, name, children, path):
        self._id = id
        self._camalis = client
        self._name = name
        self._children = children
        self._path = path

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def children(self):
        return self._children

    @property
    def path(self):
        return self._path

class CamalisElementClient:
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient):
        self._camalis = client

    def _process_element_children(self, elements: List):
        children = []
        if len(elements) > 0:
            for element in elements:
                child = Element(
                    self._camalis,
                    id=element['id'],
                    name=element['nome'],
                    children=element['filhos'],
                    path=element['path']
                )
                children.append(child)
        return children

    def get(self, name=None, path=None):

        if path is None and name is None:
            raise CamalisApiException('Name or path is required')

        if path and name:
            raise CamalisApiException('Only one parameter is allowed')

        response = None

        url = '/elementos/'

        if name:
            url = f'{url}buscarPorNome/?nome={name}'
            response = self._camalis.request_get(url=url)
            elementos = response['elementos']
            children = []

            if elementos is None:
                raise CamalisApiException('Not found elements')

            if len(elementos) == 0:
                raise CamalisApiException('Not found elements')

            elemento = elementos[0]
            elementos_filhos = elemento['filhos']

            if len(elementos_filhos) > 0:
                children = self._process_element_children(elements=elementos_filhos)

            return Element(self._camalis, elemento['id'], elemento['nome'], children, path=elemento['path'])

        if path:
            url = f'{url}buscarPorPath/?path={path}'
            response = self._camalis.request_get(url=url)
            elemento = response['elemento']
            elemento_filhos_response = response['filhos']
            children = []

            if len(elemento_filhos_response) > 0:
                children = self._process_element_children(elements = elemento_filhos_response)

            return Element(
                self._camalis,
                id=elemento['id'],
                name=elemento['nome'],
                children=children,
                path=elemento['path']
            )

        if response['elementos'] is None:
            raise CamalisApiException('Element not found')

    def list(self):
        url = '/elementos/listar/'
        response = self._camalis.request_get(url=url)
        elements = response['elementos']

        def process_element(element):
            id = element['id']
            name = element['nome']
            element_children = element['filhos']
            path = element['path']
            children = [process_element(child) for child in element_children] if element_children else []
            return Element(self._camalis, id, name, children, path=path)

        processed_elements = [process_element(element) for element in elements]

        return processed_elements