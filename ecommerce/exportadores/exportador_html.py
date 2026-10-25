
import html

from ecommerce.exportadores.exportador_relatorio import ExportadorRelatorio


class ExportadorHTML(ExportadorRelatorio):

    def criar_documento(self, relatorio: list) -> str:
        if not relatorio:
            return "<html><body><p>Relatório vazio</p></body></html>"

        colunas = relatorio[0].keys()

        documento = [
            "<html>",
            "<head><meta charset='utf-8'><title>Relatório Financeiro</title></head>",
            "<body>",
            "<h1>Relatório Financeiro</h1>",
            "<table border='1'>",
            "<thead><tr>"
        ]

        for coluna in colunas:
            documento.append(f"<th>{html.escape(str(coluna))}</th>")

        documento.append("</tr></thead><tbody>")

        for registro in relatorio:
            documento.append("<tr>")

            for coluna in colunas:
                valor = html.escape(str(registro.get(coluna, "")))
                documento.append(f"<td>{valor}</td>")

            documento.append("</tr>")

        documento.extend([
            "</tbody>",
            "</table>",
            "</body>",
            "</html>"
        ])

        return "\n".join(documento)
