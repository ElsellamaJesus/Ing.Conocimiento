"""
----------------Ejercicio 34---------------
Determinar si la suma 3^1974 + 3^1974 + 3^1974
es igual a 3^1975
"""

print("----------Comparar las sumas-------")

a = 3**1975
b = 3**1974
c = 3**1974
d = 3**1974

if (a == (b + c + d)):
    print("La suma da el mismo resultado")
else:
    print("Los valores no son los mismos")