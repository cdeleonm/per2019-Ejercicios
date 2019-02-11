import math
class Figura():
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def get_area(self):
        area = self.lado ** 2
        return area

    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_area(self):
        area = self.base * self.altura
        return area

    def get_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def get_area(self):
        area = math.pi * self.radio ** 2
        return area

    def get_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

cuad = Cuadrado(2)
rect = Rectangulo(3, 5)
circ = Circulo(3)

print("El area del cuadrado es:", cuad.get_area())
print("El area del triangulo es:", rect.get_area())
print("El area del circulo es:", circ.get_area())
print("El perimetro del cuadrado es:", cuad.get_perimetro())
print("El perimetro del triangulo es:", rect.get_perimetro())
print("El perimetro del circulo es:", circ.get_perimetro())
