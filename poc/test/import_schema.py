
import store.odufilx

print ("___upload schema__")
oduflix_path = "..//data//ODUFlix//schema.json"

print(oduflix_path)

oduflix_movies:store.odufilx.OduFlixStore = store.odufilx.OduFlixStore(oduflix_path)
print(oduflix_movies.print_content())


oduflix_movies.upload_schema()
print(oduflix_movies.schema)
print(type(oduflix_movies.schema))