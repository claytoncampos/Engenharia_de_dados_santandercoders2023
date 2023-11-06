lista =[]
lista = list()
lista = ["eu", 10, 25, "ela",False]
lista_de_lista = [10,[20,30]]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista_de_lista[0])
print(lista_de_lista[1][0])
print(lista_de_lista[1][1])


lista_top = [10,11,30,100,25,63]

print(lista_top[::])
print(lista_top[:-1])
print(lista_top[:3])
print(lista_top[-1])
print(lista_top[2:])
print(lista_top[1:])


for el in lista_top:
    print(el)


print("coprimento da lista", len(lista_top))

for i in range(len(lista_top)):
    print(i**i)

for i in range(len(lista_top)):
    print(lista_top[i])