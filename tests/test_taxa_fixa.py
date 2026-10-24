
import pytest

from ecommerce.estrategias.taxa_fixa import TaxaFixa


def test_calcular_taxa_fixa():
    estrategia = TaxaFixa(5)

    assert estrategia.calcular(100) == 95


def test_taxa_fixa_nao_ultrapassa_o_valor():
    estrategia = TaxaFixa(10)

    assert estrategia.calcular(5) == 0


def test_taxa_negativa_e_rejeitada():
    with pytest.raises(ValueError):
        TaxaFixa(-5)


def test_valor_negativo_e_rejeitado():
    estrategia = TaxaFixa(5)

    with pytest.raises(ValueError):
        estrategia.calcular(-100)
