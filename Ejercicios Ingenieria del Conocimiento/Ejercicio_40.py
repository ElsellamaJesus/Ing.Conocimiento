"""
----------------Ejercicio 40--------------
Una pulgada equivales a 2.5 cm. Calcular el
numero de cm en 32 pulgadas.
"""
print ("Convertir Pulgadas a Centimetros")
print ("Pulgada = 2.5 cm")
print("Calcular 32 pulgadas")

p = 2.5
def calcular():
    cal = p * 32
    return cal

res = calcular()
print ()
print("La Cantidad es: "+str(res) + " cm")

"""
alternativa
p = float(input("Cantidad de pulgadas a calcular?"))
cm = p * 2.5
print (str(cm) + " cm")
"""