
import pytest

from ecommerce.estrategias.juros_compostos import JurosCompostos


def test_calcular_juros_compostos():
    estrategia = JurosCompostos(2, 3)

    resultado = estrategia.calcular(1000)

    assert resultado == pytest.approx(1061.208)


def test_taxa_negativa():
    with pytest.raises(ValueError):
        JurosCompostos(-2, 3)


def test_periodos_negativos():
    with pytest.raises(ValueError):
        JurosCompostos(2, -3)
