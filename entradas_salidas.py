nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print("Hola, " + nombre + "!")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# lectura de archivos
archivo_uno = open("datos.txt", "r")
contenido = archivo_uno.read()
print(contenido)
archivo_uno.close()

# escritura de archivos
archivo_dos = open("datos.txt", "w")
archivo_dos.write("Hola, mundo!!!")
archivo_dos.close()

with open("datos.txt", "r") as archivo_tres:
    contenido = archivo_tres.read()
    print(contenido)
