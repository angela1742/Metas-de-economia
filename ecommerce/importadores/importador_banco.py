
from abc import ABC, abstractmethod


class ImportadorBanco(ABC):

    @abstractmethod
    def importar(self, registros: list) -> list:
        pass
