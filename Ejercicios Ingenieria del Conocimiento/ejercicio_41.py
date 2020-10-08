"""
----------------Ejercicio 41--------------
Una formula para cambiar Kgrs a Libras es
P = 2.2 K. donde P son Libras y K kilogramos.
Calcular el numero de libras en 212 kilogramos.
"""
print ("Convertir kg a lbs")
print ("1 libra = 2.2 kg")
print("Calcular 212 kilogramos")
p = 2.2
def calcular():
    cal = p * 212
    return cal

res = calcular()
print ()
print("La Cantidad es: "+str(res) + " lbs")

"""
alternativa
Kg = float(input("Cantidad de kg a calcular?"))
Lbs = Kg * 2.2
print (str(Lbs) + " lbs")
"""