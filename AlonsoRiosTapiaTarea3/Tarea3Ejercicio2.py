#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 22:50:10 2023

@author: Alonso
"""
print("PROGRAMA PROMEDIO NOTAS Y SEGÚN ELLAS VER SI EL ALUMNO REPROBÓ, APRÓBO O ESTA PELIGRANDO")
print("----------------------------------------------------------------------------------------")
print(" ")


numEvaluaciones = int(input("ingrese el numero de evaluaciones realizadas :"))
while numEvaluaciones < 2:
    print("¡valor incorrecto! inténtalo denuevo :")
    numEvaluaciones = int(input("ingrese el numero de evaluaciones realizadas :"))
    
print(" ")
print("evaluandose las notas desde el 1 hasta el 7:")
list = []
n = 1   #variable para imprimir la posición numerica de una nota
suma = 0 #variable destianda a ser una variable de tipo acumulador
for f in range(numEvaluaciones) :
    nota = float(input(f"ingrese la nota Nº {n} : "))
    while nota < 1 or nota > 7: #restricción
        print(" ")
        print(f"el valor de la nota Nº {n} no corresponde dentro del metodo de evaluacion, inténtelo denuevo. ")
        nota = float(input(f"ingrese la nota Nº {n} : "))
    list.append(nota)
    suma += list[f] 
    n=n+1

promedio = suma/numEvaluaciones
promedio = round(promedio,2)
if promedio >= 4.0 :
    print(f"Tu promedio es {promedio}. ¡Felicitaciones, vas camino a aprobar!")
elif promedio >= 3.0 :
    print(f"Tu promedio es {promedio}. ¡Atención, vas camino a reprobar!")
else:
    print(f"Tu promeido es {promedio}. ¡Pocas posibilidades de aprobar!")
    
    