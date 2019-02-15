#Ejercicio 2
class Contador():
    def __init__(self, numero = None):
      if numero is not None:
          self.numero = numero
      else:
          self.numero = 2

    def get_incrementar():
        return self.numero + 1

    def get_decrementar():
        return self.numero - 1

ej1 = Contador(2)
print('Si el número incrementa:', ej1.get_incrementar())
print('Si el número decrementa:', ej1.get_decrementar())

ej2 = Contador()
print('Si el número incrementa:', ej2.get_incrementar())
print('Si el número decrementa:', ej2.get_decrementar())
