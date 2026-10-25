
from ecommerce.importadores.importador_banco_x import ImportadorBancoX
from ecommerce.importadores.importador_banco_y import ImportadorBancoY


class CriadorImportador:

    @staticmethod
    def criar(banco: str):
        banco = banco.lower()

        if banco == "x":
            return ImportadorBancoX()

        if banco == "y":
            return ImportadorBancoY()

        raise ValueError(f"Banco não suportado: {banco}")
