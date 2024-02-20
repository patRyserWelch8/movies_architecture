import pandas as pd



analytical_data_path = "/Users/patryser-welch/Documents/github/movies_architecture/poc/secondary_data/streamersDataSet.csv"

data = pd.read_csv(analytical_data_path)

print("----data description :  ----")
print(data.shape)
print(data.columns)
print(data.describe())

print(data.groupby(['Classification']).describe()['Stars'])

print(data.groupby(['Streamer','Country']).count()['Title'])


