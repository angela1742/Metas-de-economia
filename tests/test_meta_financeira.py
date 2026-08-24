from datetime import date

from ecommerce.meta_dinheiro import Meta_Financeira
from ecommerce.Usuario import Usuario
from ecommerce.categoria import Categoria


class TestMetaFinanceira:

    def test_cria_meta_financeira(self):

        usuario = Usuario(1, "João")

        categoria = Categoria(1, "Lazer", "Metas de lazer")

        queijo = Meta_Financeira(
            usuario,
            1,
            "Bicicleta",
            categoria,
            "Guardar dinheiro para comprar uma bicicleta",
            13000.0,
            date(2025, 8, 13),
            date(2026, 9, 13),
            "Em andamento"
        )

        print("ID:", queijo.id)
        print("Nome:", queijo.nome)
        print("Usuário:", queijo.usuario.nome)
        print("Categoria:", queijo.categoria.nome)
        print("Descrição:", queijo.descricao)
        print("Valor objetivo:", queijo.valorObjetivo)
        print("Data de início:", queijo.dataInicio)
        print("Data de prazo:", queijo.dataPrazo)
        print("Status:", queijo.status)