
from ecommerce.estrategias.estrategia_crescimento import EstrategiaCrescimento


class CorrecaoPercentual(EstrategiaCrescimento):
    def __init__(self, taxa: float):
        if taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")

        self.taxa = taxa

    def calcular(self, valor_atual: float) -> float:
        correcao = valor_atual * self.taxa / 100
        return valor_atual + correcao
