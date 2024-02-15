import store.odufilx

print("___upload schema__")
oduflix_schema_path = "..//data//ODUFlix//schema.json"
oduflix_data_path = "..//data//ODUFlix//data.json"

print(oduflix_schema_path)

oduflix_movies: store.odufilx.OduFlixStore = store.odufilx.OduFlixStore(oduflix_schema_path,
                                                                        oduflix_data_path)
oduflix_movies.upload_schema()
oduflix_movies.upload_data()
oduflix_movies.print_data()

entry_correct : str = '{ "oduflix_catalogue" :[{ "Title": "Jurassic Park", "Producer": "Spielberg", "Year":"1992", "Classification":"Fantasy", "Stars": 5, "Actors":["Sam Neil", "Laura Dern", "Jeff G."], "Country":"USA"}]}'
entry_incorrect : str = '{ "oduflix_catalogue" :[{ "Title": "Jurassic Park", "Year":"1992", "Classification":"Fantasy", "Stars": 5, "Actors":["Sam Neil", "Laura Dern", "Jeff G."], "Country":"USA"}]}'

oduflix_movies.capture(entry_correct)
print(oduflix_movies.validate_data())
oduflix_movies.insert()
oduflix_movies.capture(entry_incorrect)
print(oduflix_movies.validate_data())
oduflix_movies.print_data()

#for key in oduflix_movies.data:
#    print(key, " - ", oduflix_movies.data[key])
#    print(type(oduflix_movies.data[key]))
