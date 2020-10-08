"""
----------------Ejercicio 35---------------
Escribir en un programa que determine las 
constantes W, X, Y y Z en la ecuacion WX + Y =
YZ - Z, e imprimir la solucion. 
"""

print ("--------Determinar una ecuacion-------")
print ("Ecuacion #1: W*X + Z = Y*Z - Z")
print ("Ecuacion #2: W = (Y*Z - Z - Y)/ X")

Res1 = 0
Res2 = 0
Res3 = 0

print("Ingresa el valor constante de la variable W")
W = float(input())
print("Ingresa el valor constante de la variable X")
X = float(input())
print("Ingresa el valor constante de la variable Y")
Y = float(input())
print("Ingresa el valor constante de la variable Z")
Z = float(input())

Res1 = W * X + Y
Res2 = Y * Z - Z

Res3 = (Y*Z-Z-Y)/X
print (" Los resultados de la ecuacion #1 son: " + str(Res1) + " = "+ str(Res2))
print (" Los resultados de la ecuacion #1 son: " + str(W) + " = " + str(Res3))