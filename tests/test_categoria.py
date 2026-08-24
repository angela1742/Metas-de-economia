from ecommerce.categoria import Categoria


class TestCategoria:

    def test_cria_categoria_com_nome(self):
        lua = Categoria(2, "www", "jjj")
        