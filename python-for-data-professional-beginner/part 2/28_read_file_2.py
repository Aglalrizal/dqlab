import requests
url = "https://dqlabcdn.xeratic.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print(response)
# Output: <Response [200]>
# Cetak isi file hello.txt menggunakan atribut response.text
print("\n>> Cetak isi file hello.txt menggunakan atribut response.text:")
print(response.text)
# #Output: 
# Kita sedang belajar Python
# Tepatnya belajar memanipulasi berkas teks
# Memanipulasi berkas dengan Python sangatlah mudah!

# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("C:\code\dqlab\python-for-data-professional-beginner\part 2\hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)
# # Output: 
# ['Kita sedang belajar Python\n', 'Tepatnya belajar memanipulasi berkas teks\n', 'Memanipulasi berkas dengan Python sangatlah mudah!']
# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("C:\code\dqlab\python-for-data-professional-beginner\part 2\hello.txt", "r")
for line in file:
    print(line)
file.close
# Output: 
# Kita sedang belajar Python

# Tepatnya belajar memanipulasi berkas teks

# Memanipulasi berkas dengan Python sangatlah mudah!
