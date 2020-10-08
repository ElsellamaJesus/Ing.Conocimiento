"""
----------------Ejercicio 38-------------------
Introducir 12 valores de A y 10 de B. Calcular
la suma de los valores A, la de los B y la suma
de los productos AB.
"""
print ("----Calcular la suma de de A y B--------")
print ("")

A = [10,11,12,13,14,15,16,17,18,19,20,21]
B = [10,11,12,13,14,15,16,17,18,19]
C = []

for i in range(len(A)):
    C.append(A[i])

for i in range(len(B)):
    C[i] = C[i] + B[i]

print("Lista A: ")
print(A)
print()
print("Lista B: ")
print(B)
print()
print("Producto AB: ")
print(C)
print()