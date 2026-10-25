
from ecommerce.servicos.servico_importacao import ServicoImportacao


class LeitorFalso:
    def ler(self, caminho):
        return [
            {
                "data": "2026-10-20",
                "valor": "100",
                "descricao": "Economia mensal"
            }
        ]


class ImportadorFalso:
    def importar(self, registros):
        return [
            {
                "data": registros[0]["data"],
                "valor": float(registros[0]["valor"]),
                "descricao": registros[0]["descricao"]
            }
        ]


class ExportadorFalso:
    def __init__(self):
        self.registros_exportados = None

    def exportar(self, relatorio, caminho):
        self.registros_exportados = relatorio


def test_servico_importacao_com_dependencias_falsas():
    leitor = LeitorFalso()
    importador = ImportadorFalso()
    exportador = ExportadorFalso()

    servico = ServicoImportacao(leitor, importador, exportador)

    resultado = servico.executar("entrada.csv", "saida.csv")

    assert len(resultado) == 1
    assert resultado[0]["valor"] == 100.0
    assert exportador.registros_exportados == resultado
