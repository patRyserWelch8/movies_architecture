import streamers_connection.odufilx
from data_management.data_store_csv import DataStoreCSV
from data_management.data_store_sql import DataStoreSQL
from streamers_connection.bigforest import BigForest

print("___upload schema__")
oduflix_schema_path = "../primary_data//ODUFlix//schema.json"
oduflix_entry_schema_path = "../primary_data//ODUFlix//schema_entry.json"

bf_schema_path = "../primary_data//BigForest//schema.json"
bf_entry_schema_path = "../primary_data//BigForest//schema_entry.json"


cdd_schema_path = "/primary_data/CCD/schema.csv"
cdd_path_path = "/primary_data/CCD/data.csv"

peartv_schema_path = "/primary_data/PearTV/ddl.sql"
peartv_data_path = "/primary_data/PearTV/movies.db"

print("___oduflix__")
print(oduflix_schema_path)

oduflix_movies: streamers_connection.odufilx.OduFlixStore = streamers_connection.odufilx.OduFlixStore(oduflix_schema_path,
                                                                                                      oduflix_entry_schema_path,
                                                                                                      None)
oduflix_movies.upload_metadata()
oduflix_movies.print_schema()

print("___big forest__")

bf_movies: BigForest = BigForest(bf_schema_path,
                                 bf_entry_schema_path,
                                 None)
bf_movies.upload_metadata()
bf_movies.print_schema()

print("___CCD__")
ccd: DataStoreCSV = DataStoreCSV(cdd_schema_path, cdd_schema_path)
ccd.upload_metadata()
ccd.print_schema()

print("___PearTV__")
sql : DataStoreSQL = DataStoreSQL(peartv_data_path, peartv_schema_path)
sql.upload_metadata()
sql.print_schema()



# 15/02/2024 all good



