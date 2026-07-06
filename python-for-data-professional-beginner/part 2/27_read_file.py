# Membaca file dengan read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open("C:\code\dqlab\python-for-data-professional-beginner\part 2\hello.txt", "r")
content = file.read()
file.close()
print(content)
# Output: 
# Kita sedang belajar Python
# Tepatnya belajar memanipulasi berkas teks
# Memanipulasi berkas dengan Python sangatlah mudah!

# Membaca file deangan readline()
print(">>> Membaca file hello.txt dengan fungsi readline()")
file = open("C:\code\dqlab\python-for-data-professional-beginner\part 2\hello.txt", "r")
first_line = file.readline()
second_line = file.readline()
print(first_line)
# Kita sedang belajar Python
print(second_line)
# Tepatnya belajar memanipulasi berkas teks

import requests
url = "https://dqlabcdn.xeratic.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print(response)
# Output: <Response [200]>
# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
	print(baris)
 
# #Output: 
# b'Kita sedang belajar Python'
# b'Tepatnya belajar memanipulasi berkas teks'
# b'Memanipulasi berkas dengan Python sangatlah mudah!'