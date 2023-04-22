#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 22:35:32 2023

@author: Alonso
"""

print("PROGRAMA PARA VERIFICAR SI UNA DIVISIÓN ES ENTERA")
print("-------------------------------------------------")
print(" ")
print("siendo a el numerador y b el denominador (a/b).")
print(" ")
a = float(input("ingrese el valor de a : "))
b = float(input("ingrese el valor de b : "))
print(" ")
while b == 0 :
    print("el numerador no puede ser 0, iténtelo denuevo.")
    b = float(input("ingrese el valor de b : "))
    print(" ")
    

#al dividir un decimal con un decimal puede darme un entero, por ende, tambien es pertiente
#comprobar
if a%b == 0:
    print(f'{a}/{b} da una división entera')
else:
    print(f'{a}/{b} no da una división entera')
