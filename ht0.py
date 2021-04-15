#ingresando la masa corporal en kg y la altura en m
print("ingrese su masa corporal en kg y su altura en m")
masa = float(input("introduzca un su masa "))
altura = float(input("introduzca su altura "))

#calculando el imc
imc = masa / (altura**2)

#redondeando a 2 decimales
imc2decimales = round(imc, 2)

#imprimiendo el imc redondeado
print("Tu índice de masa corporal es " , imc2decimales)