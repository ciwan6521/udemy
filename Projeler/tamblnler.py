# -*- coding: utf-8 -*-


def tambolenler(sayi):
    tam_bolenler = []
    
    for i in range(2,sayi):
        if (sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("Sayı: ")
    
    if (sayi == "q"):
        print("Program kapanıyor")
        break
    else:
        sayi = int(sayi)
        print("Tam Bölenler: ",tambolenler(sayi))
        
        

