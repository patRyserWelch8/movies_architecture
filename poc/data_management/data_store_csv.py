import pandas as pd

from data_management.data_store import DataStore
import pandas as pd



class DataStoreCSV(DataStore):
    def __init__(self,schema_path: str, data_path: str):
        super().__init__()
        self.schema_path: str = schema_path
        self.data_path: str = data_path

    def upload_metadata(self) -> None:
        self.schema = pd.read_csv(self.schema_path)

    def upload_date(self) -> None:
        print(self.data_path)
        self.data = pd.read_csv(self.data_path)
        print(data)

    def print_schema(self):
        print(self.schema)

