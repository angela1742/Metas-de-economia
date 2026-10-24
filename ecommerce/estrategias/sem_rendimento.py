from ecommerce.estrategias.estrategia_crescimento import EstrategiaCrescimento


class SemRendimento(EstrategiaCrescimento):
    def calcular(self, valor_atual: float) -> float:
        return valor_atual
