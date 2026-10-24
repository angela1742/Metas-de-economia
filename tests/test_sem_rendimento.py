from ecommerce.estrategias.sem_rendimento import SemRendimento


def test_sem_rendimento():
    estrategia = SemRendimento()

    resultado = estrategia.calcular(500.0)

    assert resultado == 500.0
