class DataStore (object):
    def __init__(self, schema_path: str):
        self.schema = None
        self.data  = None
        self.schema_path: str = schema_path

    def print_content(self) -> str:
        return "schema_path : " + self.schema_path

    def upload_schema(self) -> None:
        with open(self.schema_path) as schema:
            self.schema = schema.read()


