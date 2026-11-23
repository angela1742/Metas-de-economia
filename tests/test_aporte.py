
from ecommerce.aporte import Aporte


class TestAporte:

    def test_cria_aporte(self):

        aporte = Aporte(
            500.0,
            "23/08/2026",
            "Primeiro aporte"
        )

        assert aporte.id is None
        assert aporte.valor == 500.0
        assert aporte.data == "23/08/2026"
        assert aporte.descricao == "Primeiro aporte"

        print("ID:", aporte.id)
        print("Valor:", aporte.valor)
        print("Data:", aporte.data)
        print("Descrição:", aporte.descricao)

    def test_atribuir_id_aporte(self):

        aporte = Aporte(
            1000.0,
            "24/08/2026",
            "Segundo aporte"
        )

        aporte.atribuir_id(1)

        assert aporte.id == 1

        print("ID:", aporte.id)
        print("Aporte recebeu seu ID!")

    def test_valida_valor_aporte(self):

        aporte = Aporte(
            1000.0,
            "24/08/2026",
            "Segundo aporte"
        )

        assert aporte.validar_valor() is True

        print("Valor do aporte:", aporte.valor)
        print("Aporte válido!")

    def test_nao_permite_atribuir_id_duas_vezes(self):

        aporte = Aporte(
            500.0,
            "23/08/2026",
            "Primeiro aporte"
        )

        aporte.atribuir_id(1)

        try:
            aporte.atribuir_id(2)
            assert False
        except ValueError:
            assert aporte.id == 1

    def test_nao_permite_id_negativo_ou_zero(self):

        aporte = Aporte(
            500.0,
            "23/08/2026",
            "Primeiro aporte"
        )

        for id in [0, -1]:
            try:
                aporte.atribuir_id(id)
                assert False
            except ValueError:
                assert aporte.id is None
