"""
----------------Ejercicio 36---------------
Calcular z de acuerdo con la formula siguiente.
Asignar las variables numericas aprobadas.
Sean a = 4, b = 6, x = 8, y = 2 & c = 5 
cuando "corra" su programa:
z = (a+b)^3 - (x+y)^2*(a-c)^4 + 1/2*(c+x)
"""
print ("-----------Calcular z-------------")
print ("")
print ("Datos: a = 4, b = 6, x = 8, y = 2 & c = 5")
print("Ec. z = (a+b)^3 - (x+y)^2*(a-c)^4 + 1/2*(c+x)")

a = 4
b = 6
x = 8 
y = 2 
c = 5

z = ((a+b)**3) - ((x+y)**2)*((a-c**4)) + (1/2*(c+x))
print ("")
print ("El resultado es: "+str(z)) 