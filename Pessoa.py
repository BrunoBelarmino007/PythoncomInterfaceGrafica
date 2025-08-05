class Pessoa:

    "Isto é uma classe nova chamada Pessoa"

    idade = 15  

    def saudacao(self):
        print("Olá, tudo bem?")

# criando um novo objeto para a classe Pessoa

matheus = Pessoa()

# Outup(Saída) : 15
print(Pessoa.idade)  # Acessando o atributo idade da classe Pessoa
print(matheus.idade)  # Acessando o atributo idade do objeto matheus

# Outup : <function Pessoa.saudacao>
print(Pessoa.saudacao)  # Acessando o método saudacao da classe Pessoa
print(matheus.saudacao)  # Acessando o método saudacao do objeto matheus

# Outup : "Isto é uma classe nova chamada Pessoa"
print(Pessoa._doc_)  # Acessando a documentação da classe Pessoa
