
import json

from ecommerce.leitores.leitor import Leitor

class LeitorJSON(Leitor):

    def ler(self, caminho: str) -> list:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list):
            raise ValueError("O arquivo JSON deve conter uma lista de registros.")

        return dados
