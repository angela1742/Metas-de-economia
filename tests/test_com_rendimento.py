import pytest
from ecommerce.estrategias.com_rendimento import ComRendimento


def test_com_rendimento():
    estrategia = ComRendimento(2)

    resultado = estrategia.calcular(500.0)

    assert resultado == 510.0


def test_taxa_negativa():
    with pytest.raises(ValueError):
        ComRendimento(-2)
