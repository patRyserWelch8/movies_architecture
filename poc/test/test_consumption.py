from integration_streamers.data_consumption import StreamersETL

streamersData: StreamersETL = StreamersETL()
print(streamersData.schema)

streamersData.ingest()
streamersData.transform()