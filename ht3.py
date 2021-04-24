#ejercicio 1

print("__________________ Ejercicio 1 - Verificar Contraseña __________________")

def confirmar_contraseña(contraseña, confirmar):
    if confirmar.lower() == contraseña.lower():
        print("Las contraseñas coinciden")
    else:
        print("Las contraseñas no coinciden")


contraseña = input("Ingrese una contraseña: ")
confirmar = input("Ingrese de nuevo la contraseña: ")
confirmar_contraseña(contraseña, confirmar)

#Ejercicio 2
print("__________________ Ejercicio 2 - Asignacion de grupos __________________")

def asignar_grupo(nombre, sexo):
    if (nombre[0].lower() < "m") and (sexo.lower() == "femenino" or sexo.lower() == "mujer"):
        print("Grupo A")
    elif (nombre[0].lower() > "n") and (sexo.lower() == "masculino" or sexo.lower() == "hombre"):
        print("Grupo A")
    else:
        print("Grupo B")

    

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo: ")
if (sexo.lower() == "femenino") or (sexo.lower() == "mujer") or (sexo.lower() == "masculino") or (sexo.lower() == "hombre"):
    asignar_grupo(nombre, sexo)
else:
    print("revise los datos, Sugerencia: escriba masculino o femenino en el sexo")