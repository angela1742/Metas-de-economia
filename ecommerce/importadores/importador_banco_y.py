
from ecommerce.importadores.importador_banco import ImportadorBanco


class ImportadorBancoY(ImportadorBanco):

    def importar(self, registros: list) -> list:
        registros_importados = []

        for registro in registros:
            registro_importado = {
                "data": registro["data"],
                "valor": float(registro["montante"]),
                "descricao": registro["historico"]
            }

            registros_importados.append(registro_importado)

        return registros_importados
