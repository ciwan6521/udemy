# -*- coding: utf-8 -*-

print("""
******************
Kullanıcı Girişi:
******************      

""")


sys_kullanici_adi = "murat"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Şifreniz:  ")

if (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print("Parola Hatalı!")
elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Kullanıcı Adı Hatalı")
elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Girdiğiniz Bilgiler Hatalıdır")
else:
    print("Sisteme Başarılı Giriş")
    
    
    
    