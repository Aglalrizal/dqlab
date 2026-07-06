# Statement if
x = 4
if x%2==0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua") # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x%2==0: # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x%3 == 0: # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x%5==0: # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga ataupun lima")
    
jam = 13
if jam>=5 and jam<12: # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam>=12 and jam<17: # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam>=17 and jam<19: # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else: # selain kondisi di atas
    print("Selamat malam!")