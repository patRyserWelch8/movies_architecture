import streamers.odufilx
from data_management.data_store_csv import DataStoreCSV

from streamers.bigforest import BigForest
from streamers.ccd import CompactCatDay
from streamers.peartv import PearTV




oduflix_schema_path = "..//data//ODUFlix//schema.json"
oduflix_data_path = "..//data//ODUFlix//data.json"
oduflix_entry_schema = "..//data//ODUFlix//schema_entry.json"

bf_schema_path = "..//data//BigForest//schema.json"
bf_entry_schema_path = "..//data//BigForest//schema_entry.json"
bf_data_path = "..//data//BigForest//data.json"

cdd_schema_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/CCD/schema.csv"
cdd_data_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/CCD/data.csv"

peartv_schema_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/PearTV/ddl.sql"
peartv_data_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/data/PearTV/movies.db"


oduflix_movies: streamers.odufilx.OduFlixStore = streamers.odufilx.OduFlixStore(oduflix_schema_path,
                                                                                oduflix_entry_schema,
                                                                                oduflix_data_path)
print("___upload data__")
print("___oduflix__")
oduflix_movies.upload_metadata()
oduflix_movies.upload_data()
oduflix_movies.print_data()

print(oduflix_movies.entries)



entry_correct : str = '{ "Title": "Jurassic Park II", "Producer": "Spielberg", "Year":"1992", "Classification":"Fantasy", "Stars": 5, "Actors":["Sam Neil", "Laura Dern", "Jeff G."], "Country":"USA"}'

oduflix_movies.capture(entry_correct)
print(oduflix_movies.validate_data())
oduflix_movies.insert()
print(oduflix_movies.entries)

print("___BigForest__")
bf_movies: BigForest = BigForest(bf_schema_path, bf_entry_schema_path, bf_data_path)

bf_movies.upload_metadata()
bf_movies.upload_data()
bf_movies.print_data()


entry_correct : str = '{ "Title": "Diamonds never dies", "Year":"1980", "Category":"Spy movie", "Rental":0.00, "Purchase":0.00, "Stars": 3, "Classification":"15","Country":"GB"}'

bf_movies.capture(entry_correct)
bf_movies.insert()
print(bf_movies.entries)
print(bf_movies.confirm_insert_message())

print("___CCD__")

ccd: CompactCatDay = CompactCatDay(cdd_schema_path, cdd_data_path)
print(cdd_data_path)
ccd.upload_metadata()
print("-----------------")
ccd.upload_data()
print(ccd.data)

entry_correct = ["News at 10", "News", "12", "GB", 2024, "News", "BBC One"]

ccd.capture(entry_correct)
ccd.insert()
ccd.confirm_insert_message()
ccd.print_data()

print("___PearTV__")

pear: PearTV = PearTV(peartv_data_path, peartv_schema_path)

pear.upload_metadata()
pear.upload_data()
pear.print_data()

entry_correct = "7, 'The Simpsons Movie', '12', 'USA', 12.99, 19.99, 4, 2000"
pear.capture(entry_correct)
pear.insert()
pear.confirm_insert_message()
pear.upload_data()
pear.print_data()
