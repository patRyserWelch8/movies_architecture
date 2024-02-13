from store.data_store import DataStore
import json

class OduFlixStore(DataStore):
     def upload_schema(self) -> None:
         super().upload_schema()
         self.schema = json.loads(self.schema)
