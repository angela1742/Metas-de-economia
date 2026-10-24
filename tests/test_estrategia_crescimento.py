import pytest

from ecommerce.estrategias.estrategia_crescimento import EstrategiaCrescimento


def test_estrategia_base_nao_pode_ser_instanciada():
    with pytest.raises(TypeError):
        EstrategiaCrescimento()
