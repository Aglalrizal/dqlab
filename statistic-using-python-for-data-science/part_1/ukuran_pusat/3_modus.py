import pandas as pd
raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# Melihat jumlah dari masing-masing produk
print( raw_data['Produk'].value_counts())