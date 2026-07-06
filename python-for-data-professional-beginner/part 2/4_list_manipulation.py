# Fitur .append(): menambahkan item baru ke dalam list
print(">>> Fitur .append()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)
#output:
# ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']

# Fitur .clear(): menghapus semua item dalam list
print(">>> Fitur .clear()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)
#output:
# []

# Fitur .copy(): menyalin list ke list baru
print(">>> Fitur .copy()")
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1.copy()
list_makanan2.append('Opor')
list_makanan3.append('Ketoprak')
print(list_makanan1)
#output:
# ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']

print(list_makanan2)
#output:
# ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Opor']


# Fitur .count(): menghitung jumlah kemunculan item tertentu dalam list
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi)
#output:
# 4

print(score_sud) 
#output:
# 3

# Fitur .extend(): menambahkan item dari list lain ke dalam list
print(">>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)
#output:
# ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Es Teh', 'Es Jeruk', 'Es Campur']