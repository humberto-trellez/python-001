# listas
frutas = ["manzana", "platano", "pera"]

frutas.append("naranja")
print(frutas)

frutas.insert(1, "durazno")
print(frutas)

frutas.remove("manzana")
print(frutas)

fruta_eliminada = frutas.pop(2)
print(frutas)
print(fruta_eliminada)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)

# tuplas
mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.index(2))
print(mi_tupla.index(2, 2))
print(mi_tupla.index(2, 2, 4))

# diccionarios
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Mexico"}

print(persona.keys())
print(persona.values())
print(persona.items())

persona.update({"profesion": "Ingeniero"})
print(persona)

# conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)

interseccion = conjunto1 & conjunto2
print(interseccion)

diferencia = conjunto1 - conjunto2
print(diferencia)

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)

conjunto1.add(4)
print(conjunto1)

conjunto1.remove(1)
print(conjunto1)

conjunto1.discard(2)
print(conjunto1)

conjunto1.clear()
print(conjunto1)



