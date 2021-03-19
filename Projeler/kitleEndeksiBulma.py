# -*- coding: utf-8 -*-

boy = float(input("Boyunuz: "))
kilo = float(input("Kilonuz: "))


indeks = kilo / ( boy**2)

print("Vücut Kitle indeksiniz: {}".format(indeks))

if (indeks  <18.5):
    print("Zayıf")
elif (indeks >= 18.5 and indeks < 25):
    print("Normal")
elif indeks >= 25 and indeks < 30:
    print("Kilolu")
else:
    print("Obez")