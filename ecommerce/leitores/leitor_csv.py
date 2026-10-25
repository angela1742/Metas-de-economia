
import csv
from ecommerce.leitores.leitor import Leitor


class LeitorCSV(Leitor):

    def ler(self, caminho: str) -> list:
        with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            return list(leitor)
