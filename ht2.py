#Ejercicio 1 - Triangulo
print("Ejercicio 1")
x = int(input("ingrese un numero entero: "))
asterisco = "*"

i = 1
while i < (x + 1):
  print(asterisco * i)
  i += 1 

#Ejercicio 2 - Verificador de numero primo
print("----------")
print("Ejercicio 2")
num = int(input("ingrese un numero entero mayor o igual a 2 para verificar: "))

def numeroprimo(num):
    if num == 0 or num == 1:
        print("numero invalido ingrese un numero mayor o igual a 2")
    else:
        for div in range(2, num):
            if num%div == 0:
                return False                   
        return True   

primo = numeroprimo(num)
if primo == True:
    print("Es primo")
else:
    print("No es primo")           