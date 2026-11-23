
from datetime import date


class Aporte:

    def __init__(self, valor: float, data: date, descricao: str):

        if valor <= 0:
            raise ValueError("O valor do aporte deve ser maior que zero.")

        if isinstance(data, date):
            data = data.strftime("%d/%m/%Y")

        elif isinstance(data, str):
            try:
                dia, mes, ano = map(int, data.split("/"))
                date(ano, mes, dia)
            except (ValueError, TypeError):
                raise ValueError("A data do aporte deve ser válida.")

        else:
            raise ValueError("A data do aporte deve ser válida.")

        self._id = None
        self.valor = valor
        self.data = data
        self.descricao = descricao

    @property
    def id(self):
        return self._id

    def atribuir_id(self, id: int):
        if self._id is not None:
            raise ValueError("ID já atribuído.")

        if id <= 0:
            raise ValueError("O ID do aporte deve ser positivo.")

        self._id = id

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("O valor do aporte deve ser maior que zero.")

        return True
