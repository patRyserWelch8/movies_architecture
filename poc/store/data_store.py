import os
class DataStore(object):
    def __init__(self, schema_path: str, data_path: str):
        self.schema = None
        self.data = None
        self.schema_path: str = schema_path
        self.data_path: str = data_path

    def print_content(self) -> str:
        return "schema_path : " + self.schema_path

    def upload_schema(self) -> None:
        if os.path.isfile(self.schema_path):
            with open(self.schema_path) as schema:
                self.schema = schema.read()

    def upload_data(self) -> None:
        if os.path.isfile(self.data_path):
            with open(self.data_path) as data:
                self.data = data.read()

    def validate_data(self) -> bool:
        pass

    def insert(self) -> None:
        pass

    def print_schema(self):
        pass

    def print_data(self):
        pass

