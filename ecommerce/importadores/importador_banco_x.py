
from ecommerce.importadores.importador_banco import ImportadorBanco


class ImportadorBancoX(ImportadorBanco):

    def importar(self, registros: list) -> list:
        registros_importados = []

        for registro in registros:
            registro_importado = {
                "data": registro["data"],
                "valor": float(registro["valor"]),
                "descricao": registro["descricao"]
            }

            registros_importados.append(registro_importado)

        return registros_importados
