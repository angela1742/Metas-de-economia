
from datetime import date
from ecommerce.estrategias.estrategia_crescimento import EstrategiaCrescimento


class RegraDeRendimento:

    def __init__(
        self,
        nome: str,
        data_validade: date,
        estrategia: EstrategiaCrescimento
    ):
        self.nome = nome
        self.data_validade = data_validade
        self.estrategia = estrategia

    def esta_valida(self) -> bool:
        return date.today() <= self.data_validade

    def calcular_rendimento(self, valor_atual: float) -> float:
        if not self.esta_valida():
            raise ValueError("A regra de rendimento está vencida.")

        return self.estrategia.calcular(valor_atual)
