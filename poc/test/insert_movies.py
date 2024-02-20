import streamers_connection.odufilx

print("___upload schema__")
oduflix_schema_path = "../primary_data//ODUFlix//schema.json"
oduflix_data_path = "../primary_data//ODUFlix//data.json"

print(oduflix_schema_path)

oduflix_movies: streamers_connection.odufilx.OduFlixStore = streamers_connection.odufilx.OduFlixStore(oduflix_schema_path,
                                                                                                      oduflix_data_path)
print(oduflix_movies.print_content())

oduflix_movies.upload_data()
oduflix_movies.print_data()


entry_correct : str = '{ "Title": "Jurassic Park II", "Producer": "Spielberg", "Year":"1995", "Classification":"Fantasy", "Stars": 5, "Actors":["Sam Neil", "Laura Dern", "Jeff G."], "Country":"USA"}'
entry_incorrect : str = '{ "oduflix_catalogue" :[{ "Title": "Jurassic Park", "Year":"1992", "Classification":"Fantasy", "Stars": 5, "Actors":["Sam Neil", "Laura Dern", "Jeff G."], "Country":"USA"}]}'

oduflix_movies.capture(entry_correct)
print(oduflix_movies.validate_data())
#oduflix_movies.insert()
#oduflix_movies.capture(entry_incorrect)
#print(oduflix_movies.validate_data())
#oduflix_movies.print_data()

#for key in oduflix_movies.primary_data:
#    print(key, " - ", oduflix_movies.primary_data[key])
#    print(type(oduflix_movies.primary_data[key]))
