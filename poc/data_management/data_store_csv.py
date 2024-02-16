import os
import pandas as pd
from data_management.data_store import DataStore
import pandas as pd



class DataStoreCSV(DataStore):
    def __init__(self,schema_path: str, data_path: str):
        super().__init__()
        self.schema_path: str           = schema_path
        self.data_path  : str           = data_path
        self.entry      : pd.DataFrame  = None
        self.data       : pd.DataFrame  = pd.DataFrame()

    def upload_metadata(self) -> None:
        self.schema = pd.read_csv(self.schema_path)

    def upload_data(self) -> None:
        self.data = pd.read_csv(self.data_path)

    def print_schema(self):
        print(self.schema)

    def capture(self, entry:dict) -> None:
        self.entry = pd.DataFrame(entry,
                                  columns = self.data.columns,
                                  index=[len(self.data)])
        print(self.entry)

    def insert(self) -> None:
        if self.validate_data():
            self.data = pd.concat([self.data, self.entry], axis=0)
            #self.data.to_csv(self.data_path, index=False)
            print(self.data.columns)
    def validate_data(self) -> bool:
        list_col = set(self.schema.Column)
        keys     = set(self.entry.columns)
        return (keys == list_col) & \
               (self.data.shape[1] == self.entry.shape[1])