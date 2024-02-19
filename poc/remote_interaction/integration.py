import os.path
from remote_interaction import settings
import pandas as pd
from user_interaction.interaction_bigforrest import InteractionBigForest
from user_interaction.interaction_oduflix import InteractionOduFlix


class MoviesRemoteDate(object):
    CCD = 0
    ODUFLIX = 1
    BIGFOREST = 2


    def __init__(self):
        pass

    @staticmethod
    def ingest_ccd() -> pd.DataFrame:
        if os.path.isfile(settings.ccd_data_path):
            return pd.read_csv(settings.ccd_data_path)
        else:
            return pd.DataFrame()

    @staticmethod
    def ingest_oduflix() -> pd.DataFrame:
        if os.path.isfile(settings.oduflix_data_path):
            return pd.read_csv(settings.oduflix_data_path)
        else:
            return pd.DataFrame()

    @staticmethod
    def ingest_bigforest() -> pd.DataFrame:
        if os.path.isfile(settings.bf_data_path):
            return pd.read_csv(settings.bf_data_path)
        else:
            return pd.DataFrame()

    @staticmethod
    def ingest_peartv():
        if os.path.isfile(settings.peartv_data_path):
            return pd.read_csv(settings.peartv_data_path)
        else:
            return pd.DataFrame()



