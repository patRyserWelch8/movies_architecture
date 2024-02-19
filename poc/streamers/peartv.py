from data_management.data_store_sql import DataStoreSQL


class PearTV(DataStoreSQL):
    pass

    def upload_data(self) -> None:
        statement: str = "select * from Film"
        super().upload_data(statement)

    def insert(self) -> None:
        statement: str = "INSERT INTO Film"
        statement = statement + "(film_id, title, classification, country, rental, purchase, stars) "
        statement = statement + "VALUES ("
        statement = statement + self.entry
        statement = statement + ");"
        print(statement)
        super().insert(statement)
