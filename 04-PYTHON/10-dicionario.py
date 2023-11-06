dicionario = {}

dicionario = dict()

dicionario = {"nome":"clayton", "idade":33, "altura":1.89}

print(dicionario)
print(dicionario["nome"])
print(dicionario["idade"])


#add element in dictonary

dicionario["programador"] = True
print(dicionario)

#alterando um elemento do dicionario
dicionario["altura"] = 1.77
print(dicionario)


#iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

#testando existencia de uma chave no dicionario -- retorna true or false

print("peso" in dicionario)
print("altura" in dicionario)