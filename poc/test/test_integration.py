from integration_streamers.data_capture import DataCapture


backend : DataCapture = DataCapture()

entry_correct : str = '{ "Title": "Jurassic Park III", "Producer": "Spielberg", "Year":"1998", "Classification":"Fantasy", "Stars": 4, "Actors":["Sam Neil", "Jeff G."], "Country":"USA"}'
backend.insert_new_stream(entry_correct, backend.ODUFLIX)

print ("______")

entry_incorrect: str = '{ "Title": "Diamonds never dies", "Year":"1980", "Category":"Spy movie", "Rental":0.00, "Purchase":0.00, "Stars": 3, "Classification":"15","Country":"GB"}'
backend.insert_new_stream(entry_incorrect, backend.BIGFOREST)

entry_correct: str = '{ "Title": "Diamonds never dies", "Year":1980, "Category":"Spy movie", "Rental":0.00, "Purchase":0.00, "Stars": 3, "Classification":"15","Country":"GB"}'
backend.insert_new_stream(entry_correct, backend.BIGFOREST)

print ("______")
entry_correct = 'News at 10, News, 12, GB, 2024, News, BBC One'
backend.insert_new_stream(entry_correct, backend.CCD)



