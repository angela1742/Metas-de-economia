
from datetime import date, timedelta

import pytest

from ecommerce.regra_rendimento import RegraDeRendimento
from ecommerce.estrategias.com_rendimento import ComRendimento


def test_regra_de_rendimento_valida():
    estrategia = ComRendimento(5)
    regra = RegraDeRendimento(
        "Rendimento promocional",
        date.today() + timedelta(days=10),
        estrategia
    )

    assert regra.esta_valida() is True
    assert regra.calcular_rendimento(1000) == 1050


def test_regra_de_rendimento_vencida():
    estrategia = ComRendimento(5)
    regra = RegraDeRendimento(
        "Rendimento vencido",
        date.today() - timedelta(days=1),
        estrategia
    )

    assert regra.esta_valida() is False

    with pytest.raises(ValueError):
        regra.calcular_rendimento(1000)


def test_regra_valida_ate_o_dia_de_vencimento():
    estrategia = ComRendimento(5)
    regra = RegraDeRendimento(
        "Rendimento válido hoje",
        date.today(),
        estrategia
    )

    assert regra.esta_valida() is True
    assert regra.calcular_rendimento(1000) == 1050
