#Ejercicio 4

class Fraccion():
    def __init__(self, numerador1, denominador1, numerador2, denominador2):
        self.numerador1 = numerador1
        self.denominador1 = denominador1
        self.numerador2 = numerador2
        self.denominador2 = denominador2

    def get_suma():
        if denominador1 = denominador2:
            denominador = denominador1
            numerador = numerador1 + numerador2
        else:
            denominador = denominador1 * denominador2
            numerador= numerador1 * denominador2 + numerador2 * denominador1
        print(numerador, '/', denominador)
        return

        def get_resta():
            if denominador1 = denominador2:
                denominador = denominador1
                numerador = numerador1 - numerador2
            else:
                denominador = denominador1 * denominador2
                numerador= numerador1 * denominador2 - numerador2 * denominador1
            print(numerador, '/', denominador)
            return

            def get_multiplicacion():
                denominador = denominador1 * denominador2
                numerador = numerador1 * numerador2
                print(numerador, '/', denominador)
                return

            def get_division():
                denominador = denominador1 * numerador2
                numerador = numerador1 * denominador2
                return

ej1 = Fraccion(2, 3, 5, 3)
print('La suma es:', ej1.get_suma())
print('La resta es:', ej1.get_resta())
print('La multiplicacion es:', ej1.get_multiplicacion())
print('La division es:', ej1.get_division())

ej2 = Fraccion(3, 4, 1, 2)
print('La suma es:', ej2.get_suma())
print('La resta es:', ej2.get_resta())
print('La multiplicacion es:', ej2.get_multiplicacion())
print('La division es:', ej2.get_division())
