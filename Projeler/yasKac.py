# -*- coding: utf-8 -*-

yas = int(input("Yaşınızı Giriniz: "))

if yas<18:
    print("Buraya giremezsiniz")
else:
    print("İçeri buyurun")
    
    
sayi = int(input("sayı?: "))

if sayi<0:
    print("negatif")
elif sayi==0:
    print("sayı sıfır")
else:
    print("pozitif")