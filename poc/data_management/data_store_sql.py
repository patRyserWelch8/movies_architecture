import os.path
from data_management.data_store import DataStore
import sqlite3


def capture(self, entry):
    pass


class DataStoreSQL(DataStore):
    def __init__(self, db_path : str, schema_path: str):
        super().__init__()
        self.db_path : str = db_path
        self.schema_path : str = schema_path
        self.conn : sqlite3.Connection = None
        self.cursor : sqlite3.Cursor = None
        self.entry : str = None


    def _connect_to_db(self) -> None:
        try:
            if os.path.isfile(self.db_path):
                self.conn = sqlite3.connect(self.db_path)
                self.cursor =  self.conn.cursor()
        except sqlite3.Error as  e:
            print(e)

    def _disconnect_db(self) -> None:
        self.conn.commit()
        self.conn.close()


    def upload_metadata(self) -> None:
        schema: str = None
        if os.path.isfile(self.schema_path):
            with open(self.schema_path) as file:
                schema = file.read()
        self.schema = schema

    def upload_data(self, statement: str) -> None:
        self._connect_to_db()
        self.cursor.execute(statement)
        self.data = self.cursor.fetchall()
        self._disconnect_db()

    def capture(self, entry: str) -> None:
        super().capture(entry)
        self.entry = entry

    def _validate_data(self) -> bool:
        no_cols   = len(self.schema.split(","))
        no_values = len(self.entry.split(","))
        return no_values == no_cols


    def insert(self, statement : str) -> None:
        try:
            if self._validate_data():
                self._connect_to_db()
                rows = self.cursor.execute(statement)
                self._disconnect_db()
                if rows.rowcount >= 1:
                   self.status_insert = True
        except sqlite3.Error as e:
            print (e)

    def print_schema(self):
        print(self.schema)

    def print_data(self):
        print(self.data)