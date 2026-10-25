
from ecommerce.exportadores.exportador_csv import ExportadorCSV
from ecommerce.exportadores.exportador_html import ExportadorHTML


def test_exportador_csv_cria_arquivo(tmp_path):
    caminho = tmp_path / "relatorio.csv"
    relatorio = [
        {"meta": "Viagem", "valor": 500},
        {"meta": "Computador", "valor": 200}
    ]

    exportador = ExportadorCSV()
    exportador.exportar(relatorio, str(caminho))

    conteudo = caminho.read_text(encoding="utf-8")

    assert "meta,valor" in conteudo
    assert "Viagem,500" in conteudo
    assert "Computador,200" in conteudo


def test_exportador_html_cria_arquivo(tmp_path):
    caminho = tmp_path / "relatorio.html"
    relatorio = [{"meta": "Viagem", "valor": 500}]

    exportador = ExportadorHTML()
    exportador.exportar(relatorio, str(caminho))

    conteudo = caminho.read_text(encoding="utf-8")

    assert "<html>" in conteudo
    assert "Viagem" in conteudo
    assert "500" in conteudo


def test_exportador_html_escapa_conteudo():
    exportador = ExportadorHTML()
    relatorio = [{"meta": "<Viagem>", "valor": 500}]

    documento = exportador.criar_documento(relatorio)

    assert "&lt;Viagem&gt;" in documento
