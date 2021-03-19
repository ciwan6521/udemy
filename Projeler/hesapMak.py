# -*- coding: utf-8 -*-

print("""**************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi   

4. Bölme İşlemi
      

***************
""")


a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))
islem = input("İşlemi Giriniz: ")

if islem == "1":
    print("{} ile {} sayısının toplamı {}".format(a,b,a+b))
elif islem == "2":
    print("{} sayısından {} sayısını çıkarınca {}".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} sayısının çarpımı {}".format(a,b,a*b))
elif islem == "4":
    print("{} sayısının {} sayısına bölümü {}".format(a,b,a/b))
else:
    print("Geçersiz işlem.....")
    