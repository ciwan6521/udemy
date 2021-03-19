# -*- coding: utf-8 -*-

class ögretmen():
    
    def __init__(self,ad,soyad,telefon,maas,dersler):
        
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.maas = maas
        self.ders = dersler
        

    def bilgiler(self):
        print("""
              
              Öğretmenin Adı : {}
              
              Öğretmenin Soyadı : {}
              
              Öğretmenin Numarası : {}
              
              Öğretmenin Maaşı : {}
              
              Öğretmenin Bildiği Dersler : {}
              
              """.format(self.ad,self.soyad,self.telefon,self.maas,self.ders))
    def zamyap(self,zammiktarı):
        self.maas = self.maas + zammiktarı
        
Murat =  ögretmen("Murat","Kaya",123,5000,["Matematik","Fen","İngilizce"])

print(Murat.zamyap(750))

print(Murat.bilgiler())
