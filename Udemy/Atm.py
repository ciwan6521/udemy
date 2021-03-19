# -*- coding: utf-8 -*-

print(""" Atm'ye Hoşgeldiniz....
      
      Para Çekmek için : 1
      
      Para Yatırmak için : 2
      
      Bakiye Sorgulamak İçin : 3
      
      Kart iadesi için : "ç"
      
      """)
      
      
bakiye = 0


while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz...")
    
    if islem == "1":
        miktar = int(input("Çekmek istediğiniz Miktar? : "))
        if miktar > bakiye:
            print("Bakiye Yetersiz Menüye Yönlendiriliyorsunuz...")
            continue
        bakiye -= miktar
    elif islem ==  "2":
        miktar1 = int(input("Yatırmak istediğiniz Miktar? : "))
        bakiye += miktar1
    elif islem == "3":
        print("Bakiyeniz",bakiye)
    elif islem == "ç":
        print("Kartınız İade Ediliyor...")
        break
    else:
        print("Geçersiz İşlem")