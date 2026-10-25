
from abc import ABC, abstractmethod


class ExportadorRelatorio(ABC):

    def exportar(self, relatorio: list, caminho: str):
        documento = self.criar_documento(relatorio)

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(documento)

    @abstractmethod
    def criar_documento(self, relatorio: list) -> str:
        pass
