from Funcionario import Funcionario

# Cadastro inicial do funcionário
nome = input("Informe o nome do funcionário: ")
email = input("Informe o email do funcionário: ")

funcionario = Funcionario(nome, email)

# Definir quantidade de meses que serão cadastrados
qtd_meses = int(input("Quantos meses deseja cadastrar? "))

for _ in range(qtd_meses):
    mes = input("\nDigite o nome do mês: ")
    horas = float(input(f"Digite as horas trabalhadas em {mes}: "))
    salario_hora = float(input(f"Digite o salário por hora em {mes} (em R$): "))

    funcionario.cadastro_hora(mes, horas)
    funcionario.cadastroSalarioHora(mes, salario_hora)

# Mostrar informações do funcionário
print("\n--- Dados do Funcionário ---")
print(funcionario)

# Mostrar salários calculados mês a mês
print("\n--- Salários calculados ---")
for mes in funcionario.horas:
    salario = funcionario.calcularSalario(mes)
    print(f"{mes}: R$ {salario:,.2f}")
