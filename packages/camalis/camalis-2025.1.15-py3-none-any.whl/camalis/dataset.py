import io
import zipfile

import pandas as pd

from camalis.core import BaseCamalisClient
from camalis.exceptions import CamalisApiException


class CamalisDatasetClient:
    _camalis: BaseCamalisClient = None

    def __init__(self, client: BaseCamalisClient):
        self._camalis = client

    def download(self, dataset_id):
        """
        Get dataset by id
        :param dataset_id:
        :return: pandas DataFrame
        """
        if dataset_id is None:
            raise CamalisApiException('Dataset ID is required')

        url = 'dataset/download'
        response = self._camalis.request_get(
            f'/{url}/{dataset_id}', content_type='application/zip')

        zip_content = response
        all_dataframes = []

        with zipfile.ZipFile(io.BytesIO(zip_content)) as z:
            for csv_filename in z.namelist():
                if csv_filename.endswith('.csv'):
                    with z.open(csv_filename) as f:
                        df = pd.read_csv(f)
                        all_dataframes.append(df)

        combined_dataframe = pd.concat(all_dataframes, ignore_index=True)

        return combined_dataframe