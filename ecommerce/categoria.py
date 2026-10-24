class Categoria:

    def __init__(self, id: int, nome: str, descricao: str):
        if id <= 0:
            raise ValueError("O ID da categoria deve ser positivo.")

        if not nome.strip():
            raise ValueError("O nome da categoria não pode ficar vazio.")

        self.id = id
        self.nome = nome
        self.descricao = descricao
