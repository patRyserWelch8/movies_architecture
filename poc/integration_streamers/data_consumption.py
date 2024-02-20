from streamers_connection.ccd import CompactCatDay
from integration_streamers import settings
import pandas as pd
import numpy as np

from streamers_connection.peartv import PearTV


class StreamersETL:
    def __init__(self):
        self.schema = ['Streamer',
                       'Title',
                       'Classification',
                       'Country',
                       'Year',
                       'Rental',
                       'Purchase',
                       'Stars']
        self.ccd_data:  pd.DataFrame = None
        self.peartv_data : pd.DataFrame = None


    def ingest(self):
        self._ingest_ccd()
        self._ingest_peartv()

    def transform(self):
        self._transform_ccd()

    def _ingest_ccd(self):
        ccd: CompactCatDay = CompactCatDay(settings.ccd_schema_path,
                                           settings.ccd_data_path)

        ccd.upload_data()
        self.ccd_data = ccd.data

    def _ingest_peartv(self):
        peartv : PearTV = PearTV(settings.peartv_data_path,
                                 settings.peartv_schema_path)
        peartv.upload_data()
        data = pd.DataFrame(peartv.data)
        print(data)


    def _transform_ccd(self):
        self.ccd_data['Streamer'] = np.repeat('CCD', self.ccd_data.shape[0])
        self.ccd_data['Stars'] = np.repeat(0, self.ccd_data.shape[0])
        self.ccd_data['Rental'] = np.repeat(0.00, self.ccd_data.shape[0])
        self.ccd_data['Purchase'] = np.repeat(0.00, self.ccd_data.shape[0])

        print(self.ccd_data.columns)
        self.ccd_data = self.ccd_data.drop(columns=['TypeProgram','Channel','Category'])
        self.ccd_data = self.ccd_data.reindex(columns=self.schema)
        print(self.ccd_data.head())
        print(self.ccd_data.columns)


