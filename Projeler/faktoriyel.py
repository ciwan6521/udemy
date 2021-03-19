# -*- coding: utf-8 -*-

print("""***********************
Faktöriyel Hesalama Makinesi


Çıkmak için 'q' basabilirsiniz...  
***********************
""")


while True:
    sayi = (input("Sayıyı Giriniz: "))
    if (sayi == "q"):
        print("Program Kapatılıyor")
        break
    else:
        sayi = int(sayi)
        
        fac = 1
        
        for i in range(2,sayi+1):
            fac *= i
        print(fac)





















