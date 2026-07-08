import pandas as pd
raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print(raw_data.columns)