# -*- coding: utf-8 -*-

import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
tablo_oluştur()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES ('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()


isim = input("İsim: ")
yazar = input("Yazar: ")
yayınevi = input("Yayınevi: ")
sayfa_sayısı = int(input("Sayfa Sayısı: "))
veri_ekle2(isim, yazar, yayınevi, sayfa_sayısı)





con.close() # Bağlantıyı koparıyoruz.