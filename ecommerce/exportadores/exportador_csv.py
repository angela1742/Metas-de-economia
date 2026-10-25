
import csv
import io

from ecommerce.exportadores.exportador_relatorio import ExportadorRelatorio


class ExportadorCSV(ExportadorRelatorio):

    def criar_documento(self, relatorio: list) -> str:
        if not relatorio:
            return ""

        arquivo_texto = io.StringIO()
        escritor = csv.DictWriter(
            arquivo_texto,
            fieldnames=relatorio[0].keys()
        )

        escritor.writeheader()
        escritor.writerows(relatorio)

        return arquivo_texto.getvalue()
