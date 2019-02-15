#Ejercicio 5
class Complejo():
    def __init__(self, real1, imaginario1, real2, imaginario2):
        self.real1 = real1
        self.imaginario1 = imaginario1
        self.real2 = real2
        self.imaginario2 = imaginario2

        def get_suma():
            real = real1 + real2
            imaginario = imaginario1 + imaginario2
            print(real, '+', '('imaginario, 'i', ')')
            return

        def get_resta():
            real = real1 - real2
            imaginario = imaginario1 - imaginario2
            print(real, '+', '('imaginario, 'i', ')')
            return

        def get_multiplicacion():
            imaginario = real1 * imaginario2 + real2 * imaginario1
            print(real, '+', '('imaginario, 'i', ')')
            return

        def get_division():
            real = (real1 * real2 + imaginario1 * imaginario2) / (real2 **2 + imaginario2 **2)
            imaginario = (real2 * imaginario1 - real1 * imaginario2) / (real2 **2 + imaginario2 **2)
            print(real, '+', '('imaginario, 'i', ')')
            return

ej1 = Complejo(2, 3, 5, 3)
print('La suma es:', ej1.get_suma())
print('La resta es:', ej1.get_resta())
print('La multiplicacion es:', ej1.get_multiplicacion())
print('La division es:', ej1.get_division())

ej2 = Complejo(3, 4, 1, 2)
print('La suma es:', ej2.get_suma())
print('La resta es:', ej2.get_resta())
print('La multiplicacion es:', ej2.get_multiplicacion())
print('La division es:', ej2.get_division())
