# Fitur .clear(): Menghapus seluruh elemen dalam sebuah dictionary
print(">>> Fitur .clear()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
info_karyawan.clear()
print(info_karyawan)
# Output: {}

# Fitur .copy(): Menyalin dictionary
print(">>> Fitur .copy()")
info_karyawan1 = {'nama' : 'Aksara',
                  'nik' : '1211011',
                  'pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Senja'
info_karyawan2['nik'] = '1211056'
print(info_karyawan1)
# {'nama' : 'Aksara', 'nik' : '1211011', pekerjaan' : 'Data Analyst'}
print(info_karyawan2)
# {'nama' : 'Senja', 'nik' : '1211056', pekerjaan' : 'Data Analyst'}

# Fitur .keys(): Mengembalikan list dari seluruh kunci akses ("key") dari setiap elemen dalam sebuah dictionary
print(">>> Fitur .keys()")
info_karyawan = {'nama' : 'Aksara',
                 'nik' : '1211011',
                 'pekerjaan' : 'Data Analyst'}
kunci_akses = list(info_karyawan.keys())
print(kunci_akses)
# Output: ['nama', 'nik', 'pekerjaan']
# Fitur .values(): Mengembalikan list dari seluruh nilai ("value") dari setiap elemen dalam sebuah dictionary
print(">>> Fitur .values()")
value_dict = list(info_karyawan.values())
print(value_dict)
# Output: ['Aksara','1211011','Data Analyst']

# Fitur .update(): Menambahkan kunci akses ("key") dan nilai baru ("value") ke dalam sebuah dictionary
print(">>> Fitur .update()")
info_karyawan.update({'skillset':['Python', 'R']})
print(info_karyawan)
# Output: {'nama' : 'Aksara', 'nik' : '1211011', pekerjaan' : 'Data Analyst', 'skillset': ['Python', 'R']}
