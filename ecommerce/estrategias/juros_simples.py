
from ecommerce.estrategias.estrategia_crescimento import EstrategiaCrescimento


class JurosSimples(EstrategiaCrescimento):

    def __init__(self, taxa: float, periodos: int):
        if taxa < 0:
            raise ValueError("A taxa não pode ser negativa.")

        if periodos < 0:
            raise ValueError("O número de períodos não pode ser negativo.")

        self.taxa = taxa
        self.periodos = periodos

    def calcular(self, valor_atual: float) -> float:
        juros = valor_atual * (self.taxa / 100) * self.periodos
        return valor_atual + juros
