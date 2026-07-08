import pandas as pd
raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# melihat dimensi dari raw_data
print (raw_data.shape)

# mengambil jumlah data
print (raw_data.shape[0])