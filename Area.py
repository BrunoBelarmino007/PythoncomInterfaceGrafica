class Retangulo:

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarValor(self, novo_a, novo_b):
        self.lado_a = novo_a
        self.lado_b = novo_b

    def retornarValor(self):
        print(f'O Retângulo possui dimensões: {self.lado_a}m x {self.lado_b}m')

    def area(self):
        return self.lado_a * self.lado_b