import os

import jsonschema
import pandas as pd

from data_management.data_store import DataStore
import json
from jsonschema import validate


class DataStoreJSON(DataStore):

    def __init__(self, schema_path: str, entry_schema_path:str, data_path : str):
        super().__init__()
        self.data: json = {}
        self.schema: json = {}
        self.entry_json: json = None
        self.entry_schema: json = None
        self.entries : list = []
        self.root : str  = None
        self.data_df : pd.DataFrame = None

        # path to location of primary_data
        self.entry_schema_path : str = entry_schema_path
        self.schema_path       : str = schema_path
        self.data_path         : str = data_path


    @staticmethod
    def _retrieve_json(path: str) -> json:
        data_return: json = None
        if os.path.isfile(str(path)):
            with open(path) as file:
                data : str = file.read()
            if data is not None:
                data_return =  json.loads(data)
        return data_return



    def upload_metadata(self) -> None:
        self.schema = self._retrieve_json(self.schema_path)
        self.entry_schema = self._retrieve_json(self.entry_schema_path)


    def upload_data(self) -> None:
        self.data               = self._retrieve_json(self.data_path)
        if self.data.keys() is None:
            self.root = None
            self.entries = {}
        else:
            self.root = list(self.data.keys())[0]
            self.entries = self.data[self.root]

    def capture(self, entry: str) -> None:
        super().capture(entry)
        self.entry_json    = json.loads(entry)

    def _validate_data(self) -> bool:
        try:
            validate(instance=self.entry_json, schema=self.entry_schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True

    def insert(self) -> None:
        no_entries_before = len(self.entries)
        no_entries_after  = len(self.entries)
        if self._validate_data():
            self.entries.append(self.entry_json)
            no_entries_after = len(self.entries)
            self.data[self.root] = self.entries
            with open(self.data_path, 'w', encoding='utf-8') as storage:
                json.dump(self.data, storage, ensure_ascii=False, indent=4)

        self.status_insert = (no_entries_after > no_entries_before)

    def confirm_insert_message(self) -> None:
        super().confirm_insert_message()
        print(self.entry_json)

    def print_schema(self):
        print(json.dumps(self.schema, indent=2))

    def print_data(self):
        print(json.dumps(self.data, indent=2))

    def upload_data_dataframe(self) -> None:
        self.upload_data()
        self.data_df = pd.DataFrame.from_dict(self.data[self.root])



