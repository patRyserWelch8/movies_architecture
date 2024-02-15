import streamers.odufilx
from data_management.data_store_csv import DataStoreCSV
from streamers.bigforest import BigForest

print("___upload schema__")
oduflix_schema_path = "..//data//ODUFlix//schema.json"
oduflix_entry_schema_path = "..//data//ODUFlix//schema_entry.json"

bf_schema_path = "..//data//BigForest//schema.json"
bf_entry_schema_path = "..//data//BigForest//schema_entry.json"


cdd_schema_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/CCD/schema.csv"
cdd_path_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/CCD/data.csv"

print(oduflix_schema_path)

oduflix_movies: streamers.odufilx.OduFlixStore = streamers.odufilx.OduFlixStore(oduflix_schema_path,
                                                                                oduflix_entry_schema_path,
                                                                                None)
oduflix_movies.upload_metadata()
print(oduflix_movies.schema)
print(oduflix_movies.entry_schema)


bf_movies: BigForest = BigForest(bf_schema_path,
                                 bf_entry_schema_path,
                                 None)
bf_movies.upload_metadata()
print(bf_movies.schema)
print(bf_movies.entry_schema)


ccd: DataStoreCSV = DataStoreCSV(cdd_schema_path, cdd_data_path)
ccd.upload_metadata()
ccd.print_schema()




# 15/02/2024 all good



