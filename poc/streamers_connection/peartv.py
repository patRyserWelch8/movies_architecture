from data_management.data_store_sql import DataStoreSQL


class PearTV(DataStoreSQL):
    pass

    def upload_data(self) -> None:
        statement: str = "select * from Film"
        super().upload_data(statement)

    def insert(self) -> None:
        statement: str = "INSERT INTO Film"
        statement = statement + "(film_id, title, classification, country, rental, purchase, stars, year) "
        statement = statement + "VALUES ("
        statement = statement + self.entry
        statement = statement + ");"
        print(statement)
        super().insert(statement)

    def get_new_id(self) -> int:
        statement : str = "select max(film_id) from Film;"
        record = self.exectute(statement)
        return record[0][0]
