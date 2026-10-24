from abc import ABC, abstractmethod


class EstrategiaCrescimento(ABC):

    @abstractmethod
    def calcular(self, valor_atual: float) -> float:
        pass
