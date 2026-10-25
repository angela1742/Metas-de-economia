from abc import ABC, abstractmethod


class Leitor(ABC):

    @abstractmethod
    def ler(self, caminho: str) -> list:
        pass
