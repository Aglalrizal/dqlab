# Fitur .add(): Menambah data ke dalam set, data dalam set tidak boleh duplikat
print(">>> Fitur .add()") 
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.add('Melon')
print(set_buah)
# Output: 
# {'Jeruk','Apel','Anggur', 'Melon'}
# Fitur .clear(): Menghapus seluruh elemen dalam set
print(">>> Fitur .clear()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.clear()
print(set_buah)
# Output: 
# set() atau empty{}

# Fitur .copy(): Menduplikat set
print(">>> Fitur .copy()")
set_buah1 = {'Jeruk','Apel','Anggur'}
set_buah2 = set_buah1
set_buah3 = set_buah1.copy()
set_buah2.add('Melon')
set_buah3.add('Kiwi')
print(set_buah1)
# Output:
# {'Jeruk','Apel','Anggur', 'Melon'}
print(set_buah2)
# Output:
# {'Jeruk','Apel','Anggur', 'Melon'}
print(set_buah3)
# Output:
# {'Jeruk','Apel','Anggur', 'Kiwi'}


# Fitur .update(): Menambahkan elemen dari suatu set dengan set lainnya
print(">>> Fitur .update()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel1.update(parcel2)
print(parcel1)
# Output: 
# {'Anggur','Apel','Jeruk','Kiwi','Melon'}

# Fitur .pop(): Menghilangkan sebuah elemen dari set secara acak
print(">>> Fitur .pop()")
parcel = {'Anggur','Apel','Jeruk'}
buah = parcel.pop()
print(buah)
# Output: 
# 'Anggur' atau 'Apel' ataupun 'Jeruk'
print(parcel)
# Output: 
# {'Apel','Jeruk'} atau {'Anggur','Jeruk'} ataupun {'Apel','Anggur'}

# Fitur .remove(): Menghilangkan elemen dengan nilai tertentu
print(">>> Fitur .remove()")
parcel = {'Anggur','Apel','Jeruk'}
parcel.remove('Apel')
print(parcel)
# Output:
# {'Anggur','Jeruk'}
