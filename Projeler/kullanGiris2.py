# -*- coding: utf-8 -*-

print("""
******************
Kullanıcı Girişi:
******************      

""")

sys_kullanici_adi = "murat"
sys_parola = "12345"
giris_hakkı = 30
while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    parola = input("Şifreniz:  ")
    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakkı -= 1
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı")
        giris_hakkı -= 1
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Bilgiler Hatalı")
        giris_hakkı -= 1
    else:
        print("Giriş Başarılı...")
    if (giris_hakkı == 0):
        print("Giriş Hakkınız Bitti...")
        break