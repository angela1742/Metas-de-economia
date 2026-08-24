from datetime import date

class Aporte:

    def __init__(self, id: int, valor: float, data: date, descricao: str):
            self.id = id
            self.valor = valor
            self.data = data
            self.descricao = descricao

    def validar_valor(self):
          if self.valor <= 0:
                print("O valor a ser adicionado não pode ser negativo ou zero!")
