import os

import jsonschema
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

        # path to location of data
        self.entry_schema_path : str = entry_schema_path
        self.schema_path       : str = schema_path
        self.data_path         : str = data_path


    def _retrieve_json(self, path: str) -> json:
        data: str = None
        if os.path.isfile(str(path)):
            with open(path) as data:
                data = data.read()
            if data is not None:
                return json.loads(data)

    def upload_metadata(self) -> None:
        self.schema = self._retrieve_json(self.schema_path)
        self.entry_schema = self._retrieve_json(self.entry_schema_path)


    def upload_data(self) -> None:
        self.data               = self._retrieve_json(self.data_path)
        self.root               = list(self.data.keys())[0]
        self.entries            = self.data[self.root]



    def capture(self, entry: str) -> None:
        self.entry_json = json.loads(entry)

    def _validate_data(self) -> bool:
        print(self.entry_schema)
        try:
            validate(instance=self.entry_json, schema=self.entry_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def insert(self) -> None:
        if self._validate_data:
            self.entries.append(self.entry_json)
            self.data[self.root] = self.entries
            with open(self.data_path, 'w', encoding='utf-8') as storage:
                json.dump(self.data, storage, ensure_ascii=False, indent=4)




    def print_schema(self):
        print(json.dumps(self.schema, indent=2))

    def print_data(self):
        print(json.dumps(self.data, indent=2))
