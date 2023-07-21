## Información:

# Curso: IECD114 - Computación I
# Nombre: Alonso Rios
# Tarea n° 5

################
###Problema 1###
################

# ejercicio 1
def verificarCreciente(l):
  for f in range(len(l)-1):
    if l[f] > l[f+1]:
      return False

  return True
def sublistaCreciente(l):
  mejorI = 0
  mejorJ = 0
  mayorLargo = 1

  for i in range(0,len(l)-1):
    for j in range(i,len(l)):
      if verificarCreciente(l[i:(j+1)]) == True:
          print(l[i:(j+1)])
          if mayorLargo < len(l[i:(j+1)]):
              mayorLargo = len(l[i:(j+1)])
              mejorI = i
              mejorJ = j
          
  return [mejorI,mejorJ,mayorLargo]


#
#


################
###Problema 2###
################

# ejercicio 2
#l = [1,3,2,2,0,-1,-2,5]
def listaIndicesSumaDeM(l,m):
  listaIndice=[]
  for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):               # i < j , no puede ser igual
      if l[i]+l[j] == m:
        listaIndice.append([i,j])
        l[j] = (2)**(1/2)                     #<- #se cambia l[j] en raiz de 2 para que no se vuelva a comparar, si se cambia en un numero
                                                  #entero o decimal, puede darse la ocasión que calze con algún numero original de la lista
        break                                 #<- como ya encontró una suma que cumpla con la condición, se rompe el ciclo para l[i] no se repita 
#                                                 (por si hay valores indenticos a l[j])

  return listaIndice

################
###Problema 3###
################

def listaCreciente(l):
  #bubble sort
  for i in range(0,len(l)-1):
    for j in range(0,len(l)-1):
      if l[j] > l[j+1]:
        aux = l[j+1]
        l[j+1]= l[j]
        l[j] = aux
  return l

def listaDecreciente(l):
  #bubble sort
  for i in range(0,len(l)-1):
    for j in range(0,len(l)-1):
      if l[j] < l[j+1]:
        aux = l[j+1]
        l[j+1]= l[j]
        l[j] = aux
  return l

def paresmasimpares(l):
    pares = []
    impares = []
    for f in range (0,len(l)):
        if l[f]%2 == 0:
            pares.append(l[f])
        else:
            impares.append(l[f])
    listaCreciente(pares)
    listaDecreciente(impares)
    return pares+impares

################
###Problema 4###
################

# ejercicio 4

#listas de las bibliotecas de las facultades

#Para resolver este problema necesitamos un programa que compare cada elemento de una lista  
#con todos los elementos de otra.
#para ello necesitamos hacer un ciclo o un paso repetitivo, en donde vaya tomando todos los elementos
#de la lista 1. 
#para cada elemento de la lista 1 necesitamos otro ciclo que tome los valores de la lista 2
#para que pueda comparar un elemento de la lista 1 con todos los elementos de la lista 2. luego de comparar un
#elemento de la lista 1, se pasaría hacía el siguiente hasta el ultimo valor de la lista 1.
# es por esto que utilizamos el ciclo for. el de indice a representando el ciclo necesario para la lista 1
# y el de indice b para la lista 2, debido a que en sus rangos estan asignados sus largos, que aseguran que todos los
#valores sean pasados por el ciclo.
#finalmente con nuestra condición , que ve si ambos elementos son iguales, sí se cumple, entonces ambas listas comparten
#la misma cosa, por ende , la guardamos en una lista especial llamada "común" la cual nos muestra los elementos en común
#entre dos listas

lista1 = [1343432,39403,32932,394839,9238,30923]
lista2 = [3490,20930,1023902,1029320,32932]

def comunDe(l1,l2):
  comun = []
  for a in range(0,len(l1)):
    for b in range(0,len(l2)):
      if l1[a] == l2[b]:
        comun.append(l2[b])

  return "libros en comun :" , comun

print(comunDe(lista1,lista2))
    
    
################
###Problema 5###
################

#problema 5 A

# ejercicio 5 A
def suma_digitos(a):
  if a == 0:          #este será mi caso base, que permite que la función no tienda hacía el infinito
    return 0
  if a < 0:           #por si en el primer input salga un numero negativo
    print("solo se permiten valores mayores o iguales a 0")
  else:
    n = a
    a = a%10
    n = n//10        #me da la división exacta de a
    return a + suma_digitos(n) #de esta división exacta la agrego recursivamente a la función para que vaya tomando los restos para sumarlos, hasta que n = 0




#problema 5 B
def fibonacci(n):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# el fibonacci de fn por definición es el fibonacci de n-1 y el fibonacci de n-2, por ello
# se llama a la definición dos veces
# la condición del elif para que se termine la recursividad
# la primera condición (linea 151) para evitar numeros negativos

#problema 5 C
def factorial(n):
    if n < 0:
        return "no se permiten valores negativos"
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)


################
###Problema 6###
################


def conjunto(valor):
  if len(valor) == 0:
    return [[]]
  else:
    primeros = valor[0:-1] #<-toma toda la lista menos el ultimo valor, va a llegar un momento en donde 
#                          #  primeros = [] y cuando llegue a l, se terminará.
    ultimo = valor[-1]     #<-guarda el ultimo valor
    l = conjunto(primeros) #<-toma la lista menos el ultimo valor y repite hasta que la lista sea de largo 0
    n = l.copy()           #<-copia el contenido de la lista anterior sin modificar sus valores
    for f in range(0,len(l)):
      n[f] = n[f]+[ultimo] #<-n[f] y [ultimo] al sumar, se convierten en una unica lista

    l = n + l              
    return l



