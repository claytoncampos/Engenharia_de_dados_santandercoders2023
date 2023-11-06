numero_sorteado = 10

numero_escolhido = int(input("Escolha um numero de 0 a 20 "))
if numero_escolhido == numero_sorteado:
    print("ganhou")
else:
    print("voce errou")

print(10*"-")
while numero_escolhido != numero_sorteado:
    print("tente novamente")
    numero_escolhido = int(input("Escolha um numero de 0 a 20 "))
print("acertou")
print(10*"-")
nomes = ["clay", "jorge", "maria"]

for nome in nomes:
    print(nome)
print(10*"-")

for variavel in range(11):
    print(variavel)
print(10*"-")

for variavel in range(3,10):
    print(variavel)    
    
print(10*"-")
for variavel in range(3,10,3):
    print(variavel)    