from integration_streamers.data_capture import Streamers


backend : Streamers = Streamers()
print("oduflix")
entry_correct : str = '{ "Title": "Jurassic Park III", "Producer": "Spielberg", "Year":"1998", "Classification":"Fantasy", "Stars": 4, "Actors":["Sam Neil", "Jeff G."], "Country":"USA"}'
backend.insert_new_stream(entry_correct, backend.ODUFLIX)

print ("______")
print("big forest")
entry_incorrect: str = '{ "Title": "Diamonds never dies", "Year":"1980", "Category":"Spy movie", "Rental":0.00, "Purchase":0.00, "Stars": 3, "Classification":"15","Country":"GB"}'
backend.insert_new_stream(entry_incorrect, backend.BIGFOREST)



print ("______")
print("ccd")
entry_correct = 'News at 10, News, 12, GB, 2024, News, BBC One'
backend.insert_new_stream(entry_correct, backend.CCD)

print ("______")
print("PearTV")
# increase id before running script
entry_correct = "10, 'Tom and Jerry : Sherlock Holmes', 'PG', 'USA', 1.99, 2.99, 5"
backend.insert_new_stream(entry_correct, backend.PEARTV)

print(backend.peartv_streamer.get_new_id())


