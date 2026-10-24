
import pytest

from ecommerce.estrategias.taxa_gratis_acima import TaxaGratisAcimaDe


def test_cobra_taxa_abaixo_do_limite():
    estrategia = TaxaGratisAcimaDe(500, 10)

    assert estrategia.calcular(200) == 190


def test_nao_cobra_taxa_ao_atingir_o_limite():
    estrategia = TaxaGratisAcimaDe(500, 10)

    assert estrategia.calcular(500) == 500


def test_nao_cobra_taxa_acima_do_limite():
    estrategia = TaxaGratisAcimaDe(500, 10)

    assert estrategia.calcular(800) == 800


def test_valor_minimo_negativo():
    with pytest.raises(ValueError):
        TaxaGratisAcimaDe(-500, 10)


def test_taxa_negativa():
    with pytest.raises(ValueError):
        TaxaGratisAcimaDe(500, -10)


def test_valor_calculado_negativo_e_rejeitado():
    estrategia = TaxaGratisAcimaDe(500, 10)

    with pytest.raises(ValueError):
        estrategia.calcular(-100)
