#Ejercicio 7
class Empleado():
    def __init__(self, sueldo, antiguedad):
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def get_sueldo():
        if antiguedad >= 5:
            sueldo += 500
        else:
            pass
            return sueldo

    def get_impuestos():
        if sueldo >= 3000:
            impuestos = sueldo * 0.15
        else:
            impuestos = sueldo * 0.1
            return impuestos

ej1 = Empleado(2500, 4)

ej2 = Empleado(5000, 10)
print('El sueldo es:', ej2.get_sueldo())
print('Los impuestos son:', ej2.get_impuestos())

ej3 = Empleado(1500, 7)
print('El sueldo es:', ej3.get_sueldo())
print('Los impuestos son:', ej3.get_impuestos())
