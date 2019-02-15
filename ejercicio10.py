#Ejercicio 10

class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_area():
        area = base * altura
        return area

    def get_perimetro():
        perimetro = 2 * base + 2 * altura
        return perimetro

class PruebaRectangulo(Rectangulo):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_area():
        area = base * altura
        return area

    def get_perimetro():
        perimetro = 2 * base + 2 * altura
        return perimetro

ej1 = PruebaRectangulo(2, 3)
ej2 = PruebaRectangulo(5, 4)
ej3 = PruebaRectangulo(1, 3)
ej4 = PruebaRectangulo(2, 2)
ej5 = PruebaRectangulo(5, 2)
print(ej1, ej2, ej3, ej4, ej5, end='\n')
