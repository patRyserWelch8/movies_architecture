import json

import store.odufilx

print("___upload schema__")
oduflix_schema_path = "..//data//ODUFlix//schema.json"

print(oduflix_schema_path)

oduflix_movies: store.odufilx.OduFlixStore = store.odufilx.OduFlixStore(oduflix_schema_path, None)
print(oduflix_movies.print_content())
oduflix_movies.upload_schema()
print(oduflix_movies.schema)
print(type(oduflix_movies.schema))
entry_schema = oduflix_movies.schema["properties"]["oduflix_catalogue"]["items"]["properties"]
print(entry_schema)
print(json.dumps(entry_schema,indent = 2))

