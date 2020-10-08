"""
----------------Ejercicio 33---------------
Imprimir la suma y el producto de todos los
posibles pares diferentes de enteros del 15
al 20.
"""

print ("---------Suma de numeros pares------")

num = list(range(15,21))
print(num)

y = 0
y = len(num)
x = 0
res = 0

while x < y:
    if num[x]%2 == 0:
        print(str(num[x]) + " Es par, se suma")
        res = res + num[x]
    else:
        print(str(num[x]) + " Es impar, no se suma")
    x += 1
    
print (" Resultado de la suma de numeros pares: " + str(res) )

""" ------------Alternativa----------------
num_par = [x for x in num if x % 2 == 0]
sum = num_par[0] + num_par[1] + num_par[2]
print("Es la suma de los pares " + str(sum))
"""
