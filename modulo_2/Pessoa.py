class Pessoa:
    "Isto é uma classe chamada Pessoa"

    def __init__(self, nome, idade):  
        self.nome = nome
        self.idade = idade  

    def saudacao(self):
        print(f"Olá {self.nome}, tudo bem? Você tem {self.idade} anos👀.")


nome_usuario = input("Informe o seu nome: ")
idade_usuario = int(input("Informe a sua idade: "))

# Criando o objeto com os dados fornecidos
pessoa1 = Pessoa(nome_usuario, idade_usuario)

# Chamando o método
pessoa1.saudacao()
