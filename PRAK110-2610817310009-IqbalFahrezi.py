import math

alas = 5
tinggi = 12

sisi_a = tinggi
sisi_c = alas
sisi_b = int(math.sqrt(sisi_a**2 + sisi_c**2))

keliling = sisi_a + sisi_b + sisi_c
luas = int(alas * tinggi / 2)

print("Diketahui :")
print("Alas = {} cm".format(alas))
print("Tinggi = {} cm\n".format(tinggi))
print("Jawab :")
print("Sisi A = {} cm".format(sisi_a))
print("Sisi B = {} cm".format(sisi_b))
print("Sisi C = {} cm".format(sisi_c))
print("Keliling = {} cm".format(keliling))
print("Luas = {} cm".format(luas))