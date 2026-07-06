nama_produk = "Sepatu Niko"
nama_produk = nama_produk[:2] + "P" + nama_produk[3:9] + "K" + nama_produk[-1]
print(nama_produk)
# Output: SePatu NiKo
print(nama_produk[:7])
# Output: SePatu
print(nama_produk[7:])
# Output: NiKo
print(len(nama_produk))