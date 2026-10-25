
import pytest

from ecommerce.leitores.leitor_csv import LeitorCSV
from ecommerce.leitores.leitor_json import LeitorJSON
from ecommerce.leitores.criador_leitor import CriadorLeitor


def test_criar_leitor_csv():
    leitor = CriadorLeitor.criar("csv")

    assert isinstance(leitor, LeitorCSV)


def test_criar_leitor_json():
    leitor = CriadorLeitor.criar("json")

    assert isinstance(leitor, LeitorJSON)


def test_formato_nao_suportado():
    with pytest.raises(ValueError):
        CriadorLeitor.criar("xml")


def test_leitor_csv(tmp_path):
    arquivo = tmp_path / "aportes.csv"
    arquivo.write_text(
        "data,valor,descricao\n2026-10-20,100,Economia mensal\n",
        encoding="utf-8"
    )

    leitor = LeitorCSV()
    resultado = leitor.ler(str(arquivo))

    assert len(resultado) == 1
    assert resultado[0]["valor"] == "100"
    assert resultado[0]["descricao"] == "Economia mensal"


def test_leitor_json(tmp_path):
    arquivo = tmp_path / "aportes.json"
    arquivo.write_text(
        '[{"data": "2026-10-20", "valor": 100, "descricao": "Economia mensal"}]',
        encoding="utf-8"
    )

    leitor = LeitorJSON()
    resultado = leitor.ler(str(arquivo))

    assert len(resultado) == 1
    assert resultado[0]["valor"] == 100


def test_leitor_json_rejeita_objeto_em_vez_de_lista(tmp_path):
    arquivo = tmp_path / "aportes.json"
    arquivo.write_text('{"valor": 100}', encoding="utf-8")

    leitor = LeitorJSON()

    with pytest.raises(ValueError):
        leitor.ler(str(arquivo))
