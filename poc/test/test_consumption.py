from integration_streamers.data_pipeline import StreamersETL

streamersData: StreamersETL = StreamersETL()
print(streamersData.schema)

streamersData.ingest()
streamersData.transform()
streamersData.load()