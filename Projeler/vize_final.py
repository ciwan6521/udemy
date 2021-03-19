# -*- coding: utf-8 -*-

vize1 = float(input("1.Vize Notunuz: "))
vize2 = float(input("2.Vize Notunuz: "))
final = float(input("Final Notunuz: "))

genel_not = vize1*(30/100) + vize2*(30/100) + final*(40/100)

if genel_not >= 90:
    print("Notunuz : AA")
elif genel_not >= 85:
    print("Notunuz : BA")
elif genel_not >= 80:
    print("Notunuz : BB")
elif genel_not >= 75:
    print("Notunuz : CB")
elif genel_not >= 70:
    print("Notunuz : CC")
elif genel_not >= 65:
    print("Notunuz : DC")
elif genel_not >= 60:
    print("Notunuz : DD")
elif genel_not >= 55:
    print("Notunuz : FD")
elif genel_not < 55:
    print("Notunuz : FF")