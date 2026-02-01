try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()

def funcion():
    contador = 5
    if contador == 5:
        raise Exception("El valor es muy grande")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")