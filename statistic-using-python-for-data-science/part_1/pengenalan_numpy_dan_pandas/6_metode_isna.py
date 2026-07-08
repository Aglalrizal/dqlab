import pandas as pd
raw_data = pd.read_csv("https://dqlabcdn.xeratic.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print (raw_data.isna())
print (raw_data.isna().sum())

# Output: 
#     ID Pelanggan   Nama  Jenis Kelamin  Pendapatan  Produk  Harga  Jumlah   Total  Tingkat Kepuasan
# 0          False  False          False       False   False  False    False  False             False
# 1          False  False          False       False   False  False    False  False             False
# 2          False  False          False       False   False  False    False  False             False
# 3          False  False          False       False   False  False    False  False             False
# 4          False  False          False       False   False  False    False  False             False
# 5          False  False          False       False   False  False    False  False             False
# 6          False  False          False       False   False  False    False  False             False
# 7          False  False          False       False   False  False    False  False             False
# 8          False  False          False       False   False  False    False  False             False
# 9          False  False          False       False   False  False    False  False             False
# 10         False  False          False       False   False  False    False  False             False
# 11         False  False          False       False   False  False    False  False             False
# 12         False  False          False       False   False  False    False  False             False
# 13         False  False          False       False   False  False    False  False             False
# 14         False  False          False       False   False  False    False  False             False
# 15         False  False          False       False   False  False    False  False             False
# 16         False  False          False       False   False  False    False  False             False
# 17         False  False          False       False   False  False    False  False             False
# 18         False  False          False       False   False  False    False  False             False
# 19         False  False          False       False   False  False    False  False             False
# ID Pelanggan        0
# Nama                0
# Jenis Kelamin       0
# Pendapatan          0
# Produk              0
# Harga               0
# Jumlah              0
# Total               0
# Tingkat Kepuasan    0
# dtype: int64