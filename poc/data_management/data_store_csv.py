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
        dtypes = pd.read_csv('tmp.csv', nrows=1).iloc[0].to_dict()
        print(dtypes)
        self.data = pd.read_csv(self.data_path, dtype = dtypes)


    def print_schema(self):
        print(self.schema)

    def capture(self, entry:list) -> None:
        columns = list(self.schema.Column)
        self.entry = pd.DataFrame(columns=columns)
        col_indices = range(0, len(columns))
        for col in col_indices:
            self.entry.loc[0, columns[col]] = entry[col]

    def insert(self) -> None:
        self.data = pd.concat([self.data, self.entry], ignore_index=True)
        self.data.to_csv(self.data_path, index = False )

    def validate_data(self) -> bool:
        list_col = set(self.schema.Column)
        keys     = set(self.entry.columns)
        return (keys == list_col) & \
               (self.data.shape[1] == self.entry.shape[1])
