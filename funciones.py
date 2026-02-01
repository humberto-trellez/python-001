def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    :param base: la base del rectángulo
    :param altura: la altura del rectángulo
    :return: el área del rectángulo
    """
    return base * altura

print(area_rectangulo(5, 3))

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))
print(suma_variable(4, 5, 6, 7))