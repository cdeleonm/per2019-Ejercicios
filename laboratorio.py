class Laboratorio():
    def __init__(self, medicamento):
        self.medicamento = medicamento

    def get_medicamento(self):
        return self.medicamento

class Medicamento():
    def __init__(self, componente, porcentaje):
        self.componente = componente
        self.porcentaje = porcentaje

    def get_componente(self):
        return self.componente

    def get_porcentaje(self):
        return self.porcentaje

ibuprofeno = Medicamento(componente = 'hipromelosa', porcentaje = 0.1)
agidol = Medicamento(componente = 'ejemplo', porcentaje = 0.2)

laboratorio = Laboratorio(ibuprofeno, agidol)

print("El medicamento es" % laboratorio.get_medicamento())
print("El componente es" % laboratorio[0].get_componente())
print("El porcentaje de este componente es" % laboratorio[1].get_porcentaje())
