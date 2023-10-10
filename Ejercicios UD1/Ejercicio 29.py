# Escribe: "Dame un nombre y una edad"
# Lee nombre, edad
# si longitud(nombre)=0:
#   nombre= "DESCONOCIDO"
# si edad<0 o 125<edad:
#   Escribe: "Error"
# sino
#   Escribe: "Te llamas (nombre) y tienes (edad) años, te quedan aun (125-edad) años por cumplir"
#
nombre = input("Dame un nombre:")
edad = int(input("Dime la edad:"))
añosR= (125-edad)
if len(nombre)==0:
    nombre = "DESCONOCIDO"
else:
    nombre = nombre
if edad<0 or 125<edad:
    print("ERROR")
else:
    print("Te llamas",nombre,"y tienes",edad,"años, te quedan aún",añosR,"años por cumplir")