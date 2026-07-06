# Fitur .index(): Mengembalikan Indeks dari elemen pertama yang ditemukan pada list
print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud)
# Output:
# 2 


# Fitur .insert(): Menyisipkan elemen pada indeks tertenru
print(">>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3, 'Sud')
print(list_score)
# Output:
# ['Budi','Sud','Budi','Sud', 'Budi','Sud']

# Fitur .pop(): Menghilangkan elemen pada posisi tertentu
print(">>> Fitur .pop()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)
# Output:
# ['Gado-gado', 'Rendang']

# Fitur .remove(): Menghilangkan elemen dengan nilai tertentu
print(">>> Fitur .remove()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)
# Output: 
# ['Gado-gado', 'Ayam Goreng', 'Ketoprak']


# Fitur .reverse(): Membalik urutan elemen dari sebuah list
print(">>> Fitur .reverse()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)
# Output:
# ['Ketoprak', 'Rendang', 'Ayam Goreng', 'Gado-gado']


# Fitur .sort(): Mengurutkan elemen pada sebuah list, nilai default adalah ascending
print(">>> Fitur .sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu)
# Output: 
# ['Ayam Goreng', 'Gado-gado', 'Ketoprak', 'Rendang']

list_menu.sort(reverse=True)# Descending
print(list_menu)
# Output:
# ['Rendang', 'Ketoprak', 'Gado-gado', 'Ayam Goreng'] 