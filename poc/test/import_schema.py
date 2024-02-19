import streamers.odufilx
from data_management.data_store_csv import DataStoreCSV
from data_management.data_store_sql import DataStoreSQL
from streamers.bigforest import BigForest

print("___upload schema__")
oduflix_schema_path = "..//data//ODUFlix//schema.json"
oduflix_entry_schema_path = "..//data//ODUFlix//schema_entry.json"

bf_schema_path = "..//data//BigForest//schema.json"
bf_entry_schema_path = "..//data//BigForest//schema_entry.json"


cdd_schema_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/CCD/schema.csv"
cdd_path_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/CCD/data.csv"

peartv_schema_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/PearTV/ddl.sql"
peartv_data_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/PearTV/movies.db"

print("___oduflix__")
print(oduflix_schema_path)

oduflix_movies: streamers.odufilx.OduFlixStore = streamers.odufilx.OduFlixStore(oduflix_schema_path,
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



