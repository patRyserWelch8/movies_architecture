import jsonschema
from store.data_store import DataStore
import json
from jsonschema import validate


class OduFlixStore(DataStore):

    def __init__(self, schema_path: str, data_path: str):
        super().__init__(schema_path, data_path)
        self.data: dict = {}
        self.schema: dict = {}
        self.entry_json: json = None

    def upload_schema(self) -> None:
        super().upload_schema()
        self.schema = json.loads(self.schema)

    def upload_data(self) -> None:
        super().upload_data()
        self.data = json.loads(self.data)
        print("****", self.data)

    def capture(self, entry: str) -> None:
        self.entry_json = json.loads(entry)

    def validate_data(self) -> bool:
        try:
            validate(instance=self.entry_json, schema=self.schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def insert(self) -> None:
        self.data.update(self.entry_json)

    def print_schema(self):
        print(json.dumps(self.schema, indent=2))

    def print_data(self):
        print(json.dumps(self.data, indent=2))
