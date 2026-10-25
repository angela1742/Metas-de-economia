
import pytest

from ecommerce.importadores.importador_banco_x import ImportadorBancoX
from ecommerce.importadores.importador_banco_y import ImportadorBancoY
from ecommerce.importadores.criador_importador import CriadorImportador


def test_importador_banco_x():
    importador = ImportadorBancoX()

    resultado = importador.importar([
        {
            "data": "2026-10-20",
            "valor": "100",
            "descricao": "Economia mensal"
        }
    ])

    assert resultado == [
        {
            "data": "2026-10-20",
            "valor": 100.0,
            "descricao": "Economia mensal"
        }
    ]


def test_importador_banco_y():
    importador = ImportadorBancoY()

    resultado = importador.importar([
        {
            "data": "2026-10-20",
            "montante": "100",
            "historico": "Economia mensal"
        }
    ])

    assert resultado == [
        {
            "data": "2026-10-20",
            "valor": 100.0,
            "descricao": "Economia mensal"
        }
    ]


def test_criador_importador_banco_x():
    importador = CriadorImportador.criar("x")

    assert isinstance(importador, ImportadorBancoX)


def test_criador_importador_banco_y():
    importador = CriadorImportador.criar("y")

    assert isinstance(importador, ImportadorBancoY)


def test_criador_importador_banco_desconhecido():
    with pytest.raises(ValueError):
        CriadorImportador.criar("z")
