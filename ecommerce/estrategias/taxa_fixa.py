


from ecommerce.estrategias.estrategia_taxa import EstrategiaTaxa


class TaxaFixa(EstrategiaTaxa):

    def __init__(self, valor_taxa: float):
        if valor_taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")

        self.valor_taxa = valor_taxa

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")

        return max(0, valor - self.valor_taxa)
