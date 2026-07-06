# Fitur .strip(): Menghilangkan kelebihan spasi pada awal dan akhir string
print(">>> Fitur .strip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan)
# Output: halo, selamat siang!
# Fitur .lstrip(): Menghilangkan spasi pada awal string
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan)
# Output: halo, selamat siang! 
# Fitur .rstrip(): Menghilangkan spasi pada akhir string
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan)
# Output:  halo, selamat siang!