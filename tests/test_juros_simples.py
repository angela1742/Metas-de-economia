
import pytest

from ecommerce.estrategias.juros_simples import JurosSimples


def test_calcular_juros_simples():
    estrategia = JurosSimples(2, 3)

    resultado = estrategia.calcular(1000)

    assert resultado == 1060


def test_taxa_negativa():
    with pytest.raises(ValueError):
        JurosSimples(-2, 3)


def test_periodos_negativos():
    with pytest.raises(ValueError):
        JurosSimples(2, -3)
