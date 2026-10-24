
import pytest
from ecommerce.estrategias.correcao_percentual import CorrecaoPercentual


def test_correcao_percentual():
    estrategia = CorrecaoPercentual(1)

    resultado = estrategia.calcular(500.0)

    assert resultado == 505.0


def test_taxa_negativa():
    with pytest.raises(ValueError):
        CorrecaoPercentual(-1)


def test_correcao_com_taxa_zero():
    estrategia = CorrecaoPercentual(0)

    resultado = estrategia.calcular(1000)

    assert resultado == 1000
