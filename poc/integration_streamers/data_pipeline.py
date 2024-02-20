from streamers_connection.bigforest import BigForest
from streamers_connection.ccd import CompactCatDay
from integration_streamers import settings
import pandas as pd
import numpy as np

from streamers_connection.odufilx import OduFlixStore
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
        self.ccd_data       : pd.DataFrame = None
        self.peartv_data    : pd.DataFrame = None
        self.bf_data        : pd.DataFrame = None
        self.oduflix_data   : pd.DataFrame = None
        self.secondary_data : pd.DataFrame = None

    def ingest(self):
        self._ingest_ccd()
        self._ingest_peartv()
        self._ingest_bf()
        self._ingest_oduflix()

    def transform(self):
        self._transform_ccd()
        self._transform_peartv()
        self._transform_bf()
        self._transform_oduflix()

    def load(self):
        sources = [self.oduflix_data,
                   self.peartv_data,
                   self.bf_data,
                   self.ccd_data]
        self.secondary_data = pd.concat(sources, axis=0)
        self.secondary_data.to_csv(settings.analytical_data_path, index = False)

    def _ingest_ccd(self) -> None:
        ccd: CompactCatDay = CompactCatDay(settings.ccd_schema_path,
                                           settings.ccd_data_path)

        ccd.upload_data()
        self.ccd_data = ccd.data

    def _ingest_peartv(self) -> None:
        peartv: PearTV = PearTV(settings.peartv_data_path,
                                settings.peartv_schema_path)
        peartv.upload_data()
        self.peartv_data = pd.DataFrame(peartv.data)

    def _ingest_bf(self) -> None:
        bf: BigForest = BigForest(settings.bf_schema_path,
                                  settings.bf_entry_schema_path,
                                  settings.bf_data_path)
        bf.upload_metadata()
        bf.upload_data_dataframe()
        self.bf_data = bf.data_df

    def _ingest_oduflix(self) -> None:
        oduflix: OduFlixStore = OduFlixStore(settings.oduflix_schema_path,
                                             settings.oduflix_entry_schema,
                                             settings.oduflix_data_path)
        oduflix.upload_metadata()
        oduflix.upload_data_dataframe()
        self.oduflix_data = oduflix.data_df

    def _transform_ccd(self):
        self.ccd_data['Streamer'] = np.repeat('CCD', self.ccd_data.shape[0])
        self.ccd_data['Stars'] = np.repeat(0, self.ccd_data.shape[0])
        self.ccd_data['Rental'] = np.repeat(0.00, self.ccd_data.shape[0])
        self.ccd_data['Purchase'] = np.repeat(0.00, self.ccd_data.shape[0])
        self.ccd_data = self.ccd_data.drop(columns=['TypeProgram', 'Channel', 'Category'])
        self.ccd_data = self.ccd_data.reindex(columns=self.schema)

    def _transform_peartv(self):
        columns = ['id', 'Title', 'Classification', 'Country', 'Rental', 'Purchase', 'Stars', 'Year']
        self.peartv_data.columns = columns
        self.peartv_data = self.peartv_data.drop(columns=['id'])
        self.peartv_data['Streamer'] = np.repeat('PearTV', self.peartv_data.shape[0])
        self.peartv_data = self.peartv_data.reindex(columns=self.schema)

    def _transform_bf(self):
        self.bf_data['Streamer'] = np.repeat('BigForest', self.bf_data.shape[0])
        self.bf_data = self.bf_data.drop(columns=['Category'])
        self.bf_data = self.bf_data.reindex(columns=self.schema)

    def _transform_oduflix(self):
        self.oduflix_data = self.oduflix_data.drop(columns=['Producer','Actors'])
        self.oduflix_data['Streamer'] = np.repeat('OduFlix', self.oduflix_data.shape[0])
        self.oduflix_data['Rental'] = np.repeat(0.00, self.oduflix_data.shape[0])
        self.oduflix_data['Purchase'] = np.repeat(0.00, self.oduflix_data.shape[0])
        self.oduflix_data['Classification'] = np.repeat('Unknown', self.oduflix_data.shape[0])
        self.oduflix_data = self.oduflix_data.reindex(columns=self.schema)
