import pandas as pd
raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Memilih kolom 'Pendapatan' saja
print (raw_data['Pendapatan'])

# Memilih kolom 'Jenis Kelamin' dan 'Pendapatan'
print (raw_data[['Jenis Kelamin', 'Pendapatan']])