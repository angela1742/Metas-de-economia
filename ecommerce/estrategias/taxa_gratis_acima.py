
from ecommerce.estrategias.estrategia_taxa import EstrategiaTaxa


class TaxaGratisAcimaDe(EstrategiaTaxa):

    def __init__(self, valor_minimo: float, valor_taxa: float):
        if valor_minimo < 0:
            raise ValueError("O valor mínimo não pode ser negativo.")

        if valor_taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")

        self.valor_minimo = valor_minimo
        self.valor_taxa = valor_taxa

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")

        if valor >= self.valor_minimo:
            return valor

        return max(0, valor - self.valor_taxa)
