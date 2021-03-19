# -*- coding: utf-8 -*-

a = int(input("a: "))
b = int(input("b: "))

print("İlk değerler:\n a:{}\n b:{} ".format(a,b))

(a,b) = (b,a)


print("Son Durumda Değerler:\n a:{}\n b:{}\n".format(a,b))