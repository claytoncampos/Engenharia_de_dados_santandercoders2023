#METODOS DE LISTAS

lista = [1,3,5,7,89,11]

#append --> inclui no fm
lista.append(77)

print(lista)

#insert --> passa o indice e o valor

lista.insert(2,"eu")
print(lista)


lista2 = [1,2,3]
#extend -> adicona os elementos de outra lista dentro da lista origem

lista.extend(lista2)
print(lista)

#pop remove o ultimo elemento da lista ou elemento especifico do indice indicado
lista.pop() # remove o ultimo
lista.pop(3)# remove o quarto elemento
print(lista)

#remove --> remove o elemento indicado não o indice

lista.remove(11)
print(lista)

#count --> conta quantas vezes certo elemento aparece na lista

print(lista.count("eu"))

#index --> mostra em qual indice está um determinado elemento

print(lista.index(77))


#sort --> organiza a lista em ordem crescente ou reverse=True ordem inversa
print(lista.remove("eu"))
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)


#FUNÇÕES PARA LISTAS
# len()
print("LEN: ", len(lista))
# sum()
print("SUM: ", sum(lista))
# min()
print("MIN: ", min(lista))
# max()
print("MAX: ", max(lista))


