"""
----------------Ejercicio 37--------------
Encontrar el mayor numero entre N numeros 
no nulos. Su programa calculara N, contando
el numero de valores no nulos que precede a 
un cero final.
"""
import random

print ("---Encontrar Numeros no nulos----")
print ("")


def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0,1000)
      return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorios=listaAleatorios(n)
print("")
print(aleatorios)

print("")
mayor = max(aleatorios)
print ("El numero mayor es: " + str(mayor))

"""
Alternativa
print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
aleatorios = [random.randint(0,1000) for _ in range(n)]
print(aleatorios)
mayor = max(aleatorios)
print ("El numero mayor es: " + str(mayor))
"""