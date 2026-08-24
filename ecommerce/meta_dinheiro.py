from datetime import date

from ecommerce.Usuario import Usuario
from ecommerce.categoria import Categoria
from ecommerce.aporte import Aporte


class Meta_Financeira:

    def __init__(
        self,
        usuario: Usuario,
        id: int,
        nome: str,
        categoria: Categoria,
        descricao: str,
        valorObjetivo: float,
        dataInicio: date,
        dataPrazo: date,
        status: str
    ):
        self.usuario = usuario
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
        self.valorObjetivo = valorObjetivo
        self.dataInicio = dataInicio
        self.dataPrazo = dataPrazo
        self.status = status
        self.aportes = []

    def calcular_valor_atual(self):
        return sum(aporte.valor for aporte in self.aportes)

    def adicionar_aporte(self, aporte: Aporte):
        self.aportes.append(aporte)

    def calcular_valor_restante(self):
        return self.valorObjetivo - self.calcular_valor_atual()

    def verificar_status(self):
        if self.calcular_valor_atual() >= self.valorObjetivo:
            self.status = "Concluída"
        else:
            self.status = "Em andamento"