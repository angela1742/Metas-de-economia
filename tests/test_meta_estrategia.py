from ecommerce.estrategias.taxa_fixa import TaxaFixa
from ecommerce.estrategias.taxa_gratis_acima import TaxaGratisAcimaDe
from datetime import date
from datetime import timedelta
from ecommerce.regra_rendimento import RegraDeRendimento
from ecommerce.Usuario import Usuario
from ecommerce.categoria import Categoria
from ecommerce.meta_dinheiro import Meta_Financeira
from ecommerce.aporte import Aporte
from ecommerce.estrategias.sem_rendimento import SemRendimento
from ecommerce.estrategias.com_rendimento import ComRendimento


def criar_meta():
    usuario = Usuario(1, "Ana")
    categoria = Categoria(1, "Viagem", "Economizar para viajar")

    meta = Meta_Financeira(
        usuario,
        1,
        "Viagem",
        categoria,
        "Viagem de férias",
        1000.0,
        date(2026, 1, 1),
        date(2027, 1, 1),
        "Em andamento"
    )

    meta.adicionar_aporte(
        Aporte(1, 500.0, "23/08/2026", "Primeiro aporte")
    )

    return meta


def test_meta_sem_rendimento():
    meta = criar_meta()

    resultado = meta.calcular_valor_projetado(SemRendimento())

    assert resultado == 500.0


def test_meta_com_rendimento():
    meta = criar_meta()

    resultado = meta.calcular_valor_projetado(ComRendimento(2))

    assert resultado == 510.0


def test_meta_com_regra_de_rendimento_valida():
    meta = criar_meta()

    regra = RegraDeRendimento(
        "Rendimento promocional",
        date.today() + timedelta(days=10),
        ComRendimento(5)
    )

    resultado = meta.calcular_valor_com_regra(regra)

    assert resultado == 525.0


def test_meta_com_regra_de_rendimento_vencida():
    meta = criar_meta()

    regra = RegraDeRendimento(
        "Rendimento vencido",
        date.today() - timedelta(days=1),
        ComRendimento(5)
    )

    import pytest

    with pytest.raises(ValueError):
        meta.calcular_valor_com_regra(regra)


def test_meta_rejeita_objeto_que_nao_e_regra():
    meta = criar_meta()

    import pytest

    with pytest.raises(TypeError):
        meta.calcular_valor_com_regra("regra inválida")


def test_meta_calcula_aporte_liquido_com_taxa_fixa():
    meta = criar_meta()
    aporte = Aporte(2, 100.0, "24/08/2026", "Segundo aporte")

    resultado = meta.calcular_aporte_liquido(aporte, TaxaFixa(5))

    assert resultado == 95.0


def test_meta_calcula_aporte_liquido_com_taxa_gratis():
    meta = criar_meta()
    aporte = Aporte(3, 500.0, "24/08/2026", "Terceiro aporte")

    estrategia = TaxaGratisAcimaDe(500, 10)
    resultado = meta.calcular_aporte_liquido(aporte, estrategia)

    assert resultado == 500.0

