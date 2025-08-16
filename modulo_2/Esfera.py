import math

class Esfera:

    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4/3) * math.pi * (self.raio ** 3)
        return vol
    
    def area(self):
        ar = 4 * math.pi * (self.raio ** 2)
        return ar

cor1 = input("Informe a cor da primeira esfera: ")
raio1 = float(input("Informe o raio da primeira esfera (em cm): "))

cor2 = input("Informe a cor da segunda esfera: ")
raio2 = float(input("Informe o raio da segunda esfera (em cm): "))

bola = Esfera(cor1, raio1)
bola2 = Esfera(cor2, raio2)

# Resultados
print(f"\nO volume da esfera de cor {bola.cor} é: {bola.volume()} cm^3")
print(f"A área da esfera de cor {bola.cor} é: {bola.area()} cm^2")

print(f"\nO volume da esfera de cor {bola2.cor} é: {bola2.volume()} cm^3")
print(f"A área da esfera de cor {bola2.cor} é: {bola2.area()} cm^2")
