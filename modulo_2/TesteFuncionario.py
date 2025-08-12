from Funcionario import Funcionario

funcionario = Funcionario("João", "joao2gmail.com")

funcionario.cadastro_hora("Janeiro", 300)
funcionario.cadastro_hora("Fevereiro", 200)
funcionario.cadastroSalarioHora("Janeiro", 30)
funcionario.cadastroSalarioHora("Fevereiro", 30)
print(funcionario)
print(funcionario.calcularSalario("Janeiro"))
print(funcionario.calcularSalario("Fevereiro"))