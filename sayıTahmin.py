

import random

sayi = random.randint(1, 40)
can = int(input("Kaç Hakkınız olsun?: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmnininiz: "))
    puan = (100 - (100/can)) * (sayac-1)
    if sayi == tahmin:
        print("Tebrikler {}. seferde bildiniz... Toplam puanınız {}".format(sayac,puan))
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı") 
        
    if hak == 0:
        print("Hakkınız bitti.Tutulan sayı: {}".format(sayi))
        
        
