
class ServicoImportacao:

    def __init__(self, leitor, importador, exportador):
        self.leitor = leitor
        self.importador = importador
        self.exportador = exportador

    def executar(self, caminho_entrada: str, caminho_saida: str):
        registros = self.leitor.ler(caminho_entrada)

        registros_importados = self.importador.importar(registros)

        self.exportador.exportar(registros_importados, caminho_saida)

        return registros_importados
