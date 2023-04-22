#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:57:04 2023

@author: Alonso
"""
# FECHA NACIMIENTO ISAAC NEWTON
"""
Newton was born in England on Christmas Day 1642 according to the Julian calendar — 
the calendar in use in England at the time. But by the 1640s, much of the rest of
Europe was using the Gregorian calendar (the one in general use today); according 
to this calendar, Newton was born on Jan. 4, 1643.
"""
# FUENTE : 
#https://archive.nytimes.com/opinionator.blogs.nytimes.com/2008/12/23/the-ten-days-of-newton/?_r=0

#INICIO
#------------------------------------------------------------------------------
print("PROGRAMA QUE DETERMINA A TRÁVES DE UNA FECHA :")
print(" ") #espacio entre variables
print("- Cuanto falta para el natalicio de Isaac Newton")
print("- Si el año de unaa fecha ingresada corresponde a un año bisiesto")
print("- Los dias transcurridos desde principio de año")
print("------------------------------------------------------------------")

# INGRESO DE FECHA
#-----------------------------------------------------------------------------
dia = int(input("ingrese el valor numerico de algún dia : "))
mes = int(input("ingrese el valor numerico de algún mes : "))
annio = int(input("ingrese el año en el que se encuentra : "))
#-------------------------------------------------------------------------------


#LISTA DIA MESES
#meses     :  1, 2, 3,4, 5, 6, 7, 8, 9, 10, 11,12
listMeses = [31,0,31,30,31,30,31,31,30,31,30,31] # dia meses


# PASOS PARA DETERMINAR LA CANTIDAD DE DÍAS DE FEBRERO (X)
#fuente : https://learn.microsoft.com/es-es/office/troubleshoot/excel/determine-a-leap-year

if annio % 100 == 0 :
    if annio%400 == 0:
        listMeses[1] = 29
elif annio%400 != 0 :
    if annio%4 == 0 :          
        listMeses[1] = 29
    else:
        listMeses[1] = 28 
        
#-----------------------------------------------------------------------------
# PASOS PARA DELIMITAR VALORES DE LA FECHA

if annio > 1643:  #condicion para que el año no sea menor al año en que nació Newton
    if 0 < mes < 13:
        if mes in [1,3,5,7,8,10,12]:
            while dia == 0 or dia < 1 or dia > 31:
                if dia < 1 or dia > 31:
                    print("El dia ingresado no corresponde con el mes, inténtalo denuevo.")
                    dia = int(input("Ingrese nuevamente el valor numerico de algún dia : "))
        else:
            if mes in [4,6,9,11]:
                while dia == 0 or dia < 1 or dia > 30:
                    if dia < 1 or dia > 30:
                        print("El dia ingresado no corresponde con el mes, inténtalo denuevo.")
                        dia = int(input("Ingrese nuevamente el valor numerico de algún dia : "))
            else :
                if mes in [2]:
                    while dia == 0 or dia < 1 or dia > listMeses[1] :
                        if dia < 1 or dia > listMeses[1]:
                            print("El dia ingresado no corresponde con el mes, inténtalo denuevo.")
                            dia = int(input("Ingrese nuevamente el valor numerico de algún dia : "))  
    else:
        print ("mes ingresado no existe en el calendario")
        while mes < 0 or mes > 12:
            mes = int(input("ingrese nuevamente el valor del mes  : "))
else :
    print("el año que se ingresó, aun no nacía Isaac newton, intentelo denuevo.")
    while annio < 1643 :
        annio = int(input("ingrese nuevamente el año en el que se encuentra : "))
                


        
print(" ") 
print(f'fecha asignada : {dia}/{mes}/{annio}')
print(" ")

        
#------------------------------------------------------------------------------
#LISTA DIA MESES ACUMULADOS.
     
q = 0
sumes = 0 #suma meses
listsumes = []

listsumes.append(sumes)
for f in range(12) :
    sumes = sumes + listMeses[q]
    listsumes.append(sumes)
    q=q+1

# LISTA VALORES ACUMULADOS DEPENDIENDO DE SI EL AÑO ES BISIESTO O NO
#[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
#[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

#------------------------------------------------------------------------------
#CALCULO DIAS FALTANTES PARA EL NATALICIO DE ISAAC NEWTON
#------------------------------------------------------------------------------


#natalicio : adj. Dicho especialmente de una celebración: Que festeja un nacimiento.
#            adj. Perteneciente o relativo al día del nacimiento.
#fuente : https://dle.rae.es/natalicio
#natalicio de isaac newton : 4 de enero 

print("- en base al calendario gregoriano Isaac Newton nace el:")
print("  4/1/1643")
print("  en base a la fecha asignada y al natalicio de Isaac Newton:")
      


meses = [1,2,3,4,5,6,7,8,9,10,11,12]


for f in range(12):
    if mes ==  meses[0]:
        if dia < 4 :
            print(f'  faltan {4-dia} días para el natalicio de Isaac Newton.')
            break
        else:
            print(f'  faltan {(listsumes[12]-dia)+4} dias para el natalicio de Isaac newton.')
            break
#(listsumes[12]-dia))+4
#listsumes[12] = 365 o 366 - DIAS TOTALES
#dia                       - DIAS TRANSCURRIDOS
#(listsumes[12]-dia)       - DIAS QUE FALTAN PARA TERMINAR EL AÑO
#4                         - DIAS QUE FALTAN PARA EL NATALICIO DESDE PRINCIPIO DE AÑO

#si resto los dias totales de un año menos los dias transcurridos, me dará los dias que faltan
#para terminar el año. con el valor calculado que me da cuantos dias faltan para ter-
#minar el año, me quedarían sumar los dias que faltan para el natalicio desde el principio de 
#año y asì tener los días que faltan para el natalicio desde la fecha asignada
    else :
        if  mes == meses[f]:
            print(f'  faltan {(listsumes[12]-(listsumes[f]+dia))+4} dias para el natalicio de Isaac newton.')
#le agrego un valor de la lista "listsumes" ya que contiene la suma de los dias de los meses de 
#manera progresiva

# si mes == 2 entonces en "meses[f]", f == 1
# el valor  de f será de 1 tambien en mi lista "listsumes", que corresponde a 31 
# 31 son los dias de enero
# si "mes" == 2 entonces hablamos de febrero. si "listsumes[f]" == 31 entonces en:
# listsumes[f]+dia estaria sumando los dias totales del mes anterior (enero) mas los dias de fe-
# brero que fueron asignados con el input, con este valor podemos restar por los DIAS TOTALES y 
# asi tener  los DIAS QUE FALTAN PARA TERMINAR EL AÑO, para luego sumarlos con los DIAS QUE 
# FALTAN PARA EL NATALICIO DESDE EL PRINCIPIO DE AÑO y así tener los dias que faltan para el 
# natalicio desde la fecha asignada
 
#DETERMINAR SI UN AÑO ES BISIESTO O NO
print(" ")
if listMeses[1] == 29 :
    print(f"- el año {annio} es bisiesto.")
else:
    print(f"- el año {annio} no es bisiesto.")
# CALCULO DE DIAS TRANSCURRIDOS
ltm = 0
b = 1
for f in range(12):
    if mes == b:
        print(" ")
        print(f'- los dias transcurridos desde principio de año fueron {listsumes[ltm]+dia} días.')
    ltm=ltm+1
    b=b+1