
from ecommerce.leitores.criador_leitor import CriadorLeitor
from ecommerce.importadores.criador_importador import CriadorImportador
from ecommerce.exportadores.exportador_csv import ExportadorCSV
from ecommerce.exportadores.exportador_html import ExportadorHTML
from ecommerce.servicos.servico_importacao import ServicoImportacao


def criar_servico(tipo_arquivo: str, banco: str, formato_saida: str):
    leitor = CriadorLeitor.criar(tipo_arquivo)

    importador = CriadorImportador.criar(banco)

    if formato_saida.lower() == "csv":
        exportador = ExportadorCSV()
    elif formato_saida.lower() == "html":
        exportador = ExportadorHTML()
    else:
        raise ValueError(f"Formato de saída não suportado: {formato_saida}")

    return ServicoImportacao(leitor, importador, exportador)
