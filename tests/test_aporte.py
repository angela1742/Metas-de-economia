from ecommerce.aporte import Aporte


class TestAporte:

    def test_cria_aporte(self):

        aporte = Aporte(
            1,
            500.0,
            "23/08/2026",
            "Primeiro aporte"
        )

        assert aporte.id == 1
        assert aporte.valor == 500.0
        assert aporte.data == "23/08/2026"
        assert aporte.descricao == "Primeiro aporte"

        print("ID:", aporte.id)
        print("Valor:", aporte.valor)
        print("Data:", aporte.data)
        print("Descrição:", aporte.descricao)

    def test_valida_valor_aporte(self):

        aporte = Aporte(
            2,
            1000.0,
            "24/08/2026",
            "Segundo aporte"
        )

        aporte.validar_valor()

        print("Valor do aporte:", aporte.valor)
        print("Aporte válido!")