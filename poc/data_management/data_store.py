import os


class DataStore(object):
    def __init__(self):
        self.schema = None
        self.data = None




    def upload_data(self) -> None:
        pass

    def upload_metadata(self) -> None:
        pass

    def validate_data(self) -> bool:
        pass

    def insert(self) -> None:
        pass

    def print_schema(self):
        pass

    def print_data(self):
        pass

    def capture(self, entry: str) -> None:
        pass