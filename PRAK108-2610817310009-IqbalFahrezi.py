import math

putaran = 5
jarak = 14
keliling = jarak / putaran
jari_jari = keliling / (2 * math.pi)

print("Diketahui : ")
print("Pak Dengklek mengelilingi taman = {} Putaran".format(putaran))
print("Jarak tempuh Pak Dengklek = {} Kilometer\n".format(jarak))
print("Jawaban : ")
print("Jari-jari taman yang dikelilingi Pak Dengklek adalah {:.2f} Kilometer".format(jari_jari))