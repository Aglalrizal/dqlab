# Fitur .startswith(): Mengembalikan nilai kebenaran True ketika sebuah teks (string) diawali dengan sebuah teks lainnya.
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
# Output: True
print(teks.startswith("apel"))
# Output: False
# Fitur .endswith(): Mengembalikan nilai kebenaran True ketika sebuah teks (string) diakhiri dengan sebuah teks lainnya.
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
# Output: True
print(teks.endswith("apel"))
# Output: False