# Fitur .count(): Mengembalikan jumlah kemunculan elemen 
print(">>> Fitur .count()")
tuple_score = ('Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud')
score_budi = tuple_score.count('Budi')
print(score_budi) # akan menampilkan output 4
# Output:
# 4
score_sud = tuple_score.count('Sud')
print(score_sud) # akan menampilkan output 3
# Output:
#3

# Fitur .index(): Mengembalikan indesk dari elemen pertama yang ditemukan
print(">>> Fitur .index()")
tuple_score = ('Budi','Sud','Budi','Budi','Budi','Sud','Sud')
score_pertama_sud = tuple_score.index('Sud')+1
print(score_pertama_sud)
# Output:
# 2