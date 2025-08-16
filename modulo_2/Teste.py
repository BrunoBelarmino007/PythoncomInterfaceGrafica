from Funcionalidades import *

# Usuário informa fabricante e modelo
fabricante = input("Informe o fabricante da TV: ")
modelo = input("Informe o modelo da TV: ")

tv = Televisor(fabricante, modelo)
controle = ControleRemoto(tv)

# Usuário pode cadastrar canais
while True:
    canal = input("Digite um canal para sintonizar (ou 'sair' para encerrar): ")
    if canal.lower() == 'sair':
        break
    controle.sintonizaCanal(canal)

# Usuário escolhe qual canal assistir
canal_troca = input("Digite o canal que deseja assistir: ")
controle.trocaCanal(canal_troca)

# Usuário ajusta o volume
valor = int(input("Digite o valor para aumentar o volume: "))
controle.aumentaVolume(valor)

valor = int(input("Digite o valor para diminuir o volume: "))
controle.diminuiVolume(valor)

# Resultado final
print("\n Informações da TV:")
print("Fabricante:", tv.fabricante)
print("Modelo:", tv.modelo)
print("Canais sintonizados:", tv.lista_de_canais)
print("Canal atual:", tv.canal_atual)
print("Volume atual:", tv.volume)
