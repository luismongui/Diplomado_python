#import  math as m
from math import sqrt,hypot
print("$"*230)
ca= float(input("ingrese dato 1"))
co =float(input("ingrese dato 2"))
#print("la hipotenusa es",m.sqrt(ca**2 + co**2))
#print("la hipotenusa nuevamente",m.hypot(ca,co))
print("la hipotenusa es",sqrt(ca**2 + co**2))
print("la hipotenusa nuevamente",hypot(ca,co))


