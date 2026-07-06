# Fitur .split(): Memecah sebuah string berdasarkan string lainnya ke dalam sebuah list
print(">>> Fitur .split()")
frasa = "ani dan budi dan wati dan johan"
karakter = frasa.split('dan')
print(karakter)
# Output: ['ani', 'budi', 'wati', 'johan']
kata = frasa.split(" ")
print(kata)
# Output: ['ani', 'dan', 'budi', 'dan', 'wati', 'dan', 'johan']
# Fitur .join(): Menggabungkan sebuah list yang berisikan string berdasarkan sebuah string yang telah didefinisikan.
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
frasa = pemisah.join(karakter)
print(frasa)
# Output: 'Ricky dan Peter dan Jordan'
frasa = " ".join(karakter)
print(frasa)
# Output: 'Ricky Peter Jordan'
# Fitur .replace(): Menggantikan kemunculan suatu string tertentu dengan string lainnya dalam sebuah string.
print(">>> Fitur .replace()")
frasa = "apel malang apel yang paling segar, apel sehat, apel nikmat"
frasa = frasa.replace("apel", "jeruk")
print(frasa)
# Output: "jeruk malang jeruk yang paling segar, jeruk sehat, jeruk nikmat" 