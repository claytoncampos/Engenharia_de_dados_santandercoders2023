#função Inicial

def saudacao():
    print("ola seja bem vindo.")

    print("ADA tecnologia - santander coders 2023")


saudacao()

#fucnao com parametro default
def saudacao2(nome, curso="Python"):
    print("ola seja bem vindo.")

    print("ADA tecnologia - santander coders 2023")

    print(nome,curso)


saudacao2("clayton")