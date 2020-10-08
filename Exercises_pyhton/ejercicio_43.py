"""
----------------Ejercicio 43--------------
Si una impresora mueve papel con una rapidez
de 1,000 pies por minuto. Cual es su rapidez 
en centimetros por segundo?
"""
print ("Calcular de ft/min a cm/seg")
print ("Datos: 1,000 ft/min a ?? cm/seg")
print ("1 ft = 30.48 cm, 1 min = 60 seg")

ft_min = float(input("Ingrese la cantidad a convertir... "))

ft = ft_min

cm = ft * 30.48

seg = cm/60

res = seg

print (str(ft_min) + " ft/min es igual a "+str(res) + " cm/seg")
