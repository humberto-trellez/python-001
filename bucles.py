frutas = ["manzana", "platano", "naranja"]

for fruta in frutas:
    print (fruta)

contador = 0

while contador < 5:
    print (contador)
    contador += 1

contador = 0

while True:
    print (contador)
    contador += 1

    if contador == 3:
        break

for i in range(10):
    if i % 2 == 0:
        continue
    print (i)

for i in range(5):
    pass