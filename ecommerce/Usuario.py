
class Usuario:

    def __init__(self, id: int, nome: str):
        if id <= 0:
            raise ValueError("O ID do usuário deve ser positivo.")

        if not nome.strip():
            raise ValueError("O nome do usuário não pode ficar vazio.")

        self.id = id
        self.nome = nome
