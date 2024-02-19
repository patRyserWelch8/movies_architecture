from integration_streamers import settings
from streamers.bigforest import BigForest
from streamers.ccd import CompactCatDay
from streamers.odufilx import OduFlixStore
from streamers.peartv import PearTV


class Streamers:
    """"
    " Those values will guide the call to direct the stream
    " data to the most appropriate streamer
    """
    CCD: int = 0
    ODUFLIX = 1
    BIGFOREST = 2
    PEARTV = 3

    def __init__(self):
        self.peartv_streamer: PearTV = PearTV(settings.peartv_data_path,
                                     settings.peartv_schema_path)


    def insert_new_stream(self, stream_data: str, provider: int):
        if provider == self.CCD:
            self._insert_ccd(stream_data)
        elif provider == self.ODUFLIX:
            self._insert_oduflix(stream_data)
        elif provider == self.BIGFOREST:
            self._insert_bigforest(stream_data)
        elif provider == self.PEARTV:
            self._insert_peartv(stream_data)


    def _insert_oduflix(self,stream_data: str) -> None:
        oduflix: OduFlixStore = OduFlixStore(settings.oduflix_schema_path,
                                             settings.oduflix_entry_schema,
                                             settings.oduflix_data_path)
        oduflix.upload_metadata()
        oduflix.upload_data()
        oduflix.capture(stream_data)
        oduflix.insert()
        oduflix.confirm_insert_message()



    def _insert_ccd(self,stream_data: str) -> None:
        stream_data_ls : list = stream_data.split(",")
        print(stream_data_ls)
        ccd: CompactCatDay = CompactCatDay(settings.ccd_schema_path,
                                           settings.ccd_data_path)
        ccd.upload_metadata()
        ccd.upload_data()
        ccd.capture(stream_data_ls)
        ccd.insert()
        ccd.confirm_insert_message()


    def _insert_bigforest(self,stream_data: str) -> None:
        bf_movies: BigForest = BigForest(settings.bf_schema_path,
                                         settings.bf_entry_schema_path,
                                         settings.bf_data_path)
        bf_movies.upload_metadata()
        bf_movies.upload_data()
        bf_movies.capture(stream_data)
        bf_movies.insert()
        bf_movies.confirm_insert_message()

    def _insert_peartv(self, stream_data: str) -> None:
        peartv : PearTV = PearTV(settings.peartv_data_path,
                                 settings.peartv_schema_path)
        peartv.upload_metadata()
        # The data is stored in the sql db. So not need to upload it
        peartv.capture(stream_data)
        peartv.insert()
        peartv.confirm_insert_message()


