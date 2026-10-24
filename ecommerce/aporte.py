from datetime import date


class Aporte:

    def __init__(self, id: int, valor: float, data: date, descricao: str):
        if id <= 0:
            raise ValueError("O ID do aporte deve ser positivo.")

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

        self.id = id
        self.valor = valor
        self.data = data
        self.descricao = descricao

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("O valor do aporte deve ser maior que zero.")

        return True
