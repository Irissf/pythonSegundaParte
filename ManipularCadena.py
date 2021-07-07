nombreDeUsuario = input("Introduce el nobre de usuario: ")

#minusculas
print(nombreDeUsuario.lower())
#mayusculas
print(nombreDeUsuario.upper())
#primera letra en mayúscula
print(nombreDeUsuario.capitalize())

edad = input("Introduce la edad: ")
#saber si es un dato numérico, devuelve true o false
print(edad.isdigit())
if (edad.isdigit() and int(edad)<18):
    print("Es menor de edad")
