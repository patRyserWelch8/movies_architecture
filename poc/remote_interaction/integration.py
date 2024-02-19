import os.path

from remote_interaction.integration_ccd import IntegrationCCD
import settings
import pandas as pd
from user_interaction.interaction_bigforrest import InteractionBigForest
from user_interaction.interaction_oduflix import InteractionOduFlix


class IngestionMovies(object):
    CCD = 0
    ODUFLIX = 1
    BIGFOREST = 2

    def __init__(self):
        self.typeOfStream: int = -1

    def ingest_ccd(self) -> pd.DataFrame:
        if os.path.isfile(settings.ccd_data_path):
            return pd.read_csv(settings.ccd_data_path)
        else:
            return pd.DataFrame()





