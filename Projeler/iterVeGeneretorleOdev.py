# -*- coding: utf-8 -*-

class Kareler():
    def __init__(self,maksimum):
        self.maksimum = maksimum
        self.sayı = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.sayı <= self.maksimum:
            sonuc = self.sayı ** 2
            self.sayı += 1
            return sonuc
        else:
            self.sayı = 1
            raise StopIteration
Kareler = Kareler(5)
for i in Kareler:
    print(i)
    
    
    
    
#%%


def asalMi(sayi):
    i = 2
    
    while (i < sayi):
        if (sayi % i == 0):
            return False
        i += 1
    return True
def asalGenerator():
    i = 2
    while True:
        if (asalMi(i)):
            yield i 
        i += 1
for sayi in asalGenerator():
    if (sayi > 1000):
        break
    print(sayi)
        
        
        
        
        
        
        
        
        
        
        
    

    