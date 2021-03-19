# -*- coding: utf-8 -*-

print("""***************
xxxxx  Atmsine Hoşgeldiniz.

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Kart iadesi için 'q' basın

***************
""")


bakiye = 4000

while True:
    islem = input("İşlemi seçiniz: ")
    
    if (islem == "q"):
        print("Yine Bekleriz")
        break
    elif (islem == "1"):
        print("Bakiyeniz: {} tl'dir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        bakiye += miktar
    elif (islem == "3"):
        miktar1 = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if (bakiye - miktar1 < 0):
            print("Bakiye yeterli değil")
            continue
        bakiye -= miktar1
    else:
        print("Geçersiz İşlem")
        
        
        
        
        
        