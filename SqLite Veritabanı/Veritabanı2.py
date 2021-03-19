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
def verileri_al():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verileri_al2():
    cursor.execute("SELECT İsim,Yazar FROM kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def verileri_al3(yayınevi):
    cursor.execute("SELECT * FROM kitaplık WHERE Yayınevi = ?", (yayınevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)
verileri_al3("Everest")
con.close() # Bağlantıyı koparıyoruz.