
from abc import ABC, abstractmethod


class EstrategiaTaxa(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass
