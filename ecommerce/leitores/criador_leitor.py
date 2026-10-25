
from ecommerce.leitores.leitor_csv import LeitorCSV
from ecommerce.leitores.leitor_json import LeitorJSON


class CriadorLeitor:

    @staticmethod
    def criar(tipo: str):
        tipo = tipo.lower()

        if tipo == "csv":
            return LeitorCSV()

        if tipo == "json":
            return LeitorJSON()

        raise ValueError(f"Formato de arquivo não suportado: {tipo}")
