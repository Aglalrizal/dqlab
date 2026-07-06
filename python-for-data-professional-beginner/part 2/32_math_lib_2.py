# Import library math
import math
# Fungsi math.log(): Menerima input berupa dua buah bilangan (asumsikan x dan y) dan mengembalikan sebuah bilangan (z) di mana z merupakan hasil log basis y dari x (atau dengan kata lain x merupakan hasil pemangkatan dari z terhadap y)
print(">>> Fungsi math.log()")
# x = log basis 2 dari 8
x = math.log(8,2)
# y = log basis 3 dari 81
y = math.log(81,3)
# z = log basis 10 dari 10000
z = math.log(10000,10)
print(x)
# 3.0
print(y)
# 4.0
print(z)
# 4.0
# Fungsi math.sqrt(): Menerima input berupa sebuah bilangan dan mengembalikan hasil akar pangkat dua (akar kuadrat) dari bilangan tersebut
print(">>> Fungsi math.sqrt()")
# akar kuadrat dari 100
x = math.sqrt(100)
print(x)
# 10.0
# akar kuadrat dari 2
y = math.sqrt(2)
print(y)
# 1.4142135623730951
# Fungsi math.copysign(): Menerima input berupa dua buah bilangan dan mengembalikan bilangan pertama sesuai dengan tanda yang dimiliki oleh bilangan kedua
print(">>> Fungsi math.copysign()")
x = 10.32
y = -13.87
z = -15
x = math.copysign(x, z)
y = math.copysign(y, z)
z = math.copysign(z, 10)
print(x)
# -10.32
print(y)
# -13.87
print(z)
# 15.0