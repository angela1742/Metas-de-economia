from ecommerce.estrategias.estrategia_taxa import EstrategiaTaxa
from ecommerce.regra_rendimento import RegraDeRendimento
from datetime import date
from ecommerce.estrategias.estrategia_crescimento import EstrategiaCrescimento
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
        if id <= 0:
            raise ValueError("O ID da meta deve ser positivo.")

        if not nome.strip():
            raise ValueError("O nome da meta não pode ficar vazio.")

        if valorObjetivo <= 0:
            raise ValueError("O valor objetivo deve ser maior que zero.")

        if not isinstance(dataInicio, date):
            raise ValueError("A data de início deve ser válida.")

        if not isinstance(dataPrazo, date):
            raise ValueError("A data do prazo deve ser válida.")

        if dataPrazo < dataInicio:
            raise ValueError("O prazo não pode ser anterior ao início.")

        self.usuario = usuario
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
        self.valorObjetivo = valorObjetivo
        self.dataInicio = dataInicio
        self.dataPrazo = dataPrazo
        self.aportes = []

        self.status = "Em andamento"
        self.verificar_status()

    def calcular_valor_atual(self):
        return sum(aporte.valor for aporte in self.aportes)

    def adicionar_aporte(self, aporte: Aporte):
        if not isinstance(aporte, Aporte):
            raise TypeError("É necessário adicionar um objeto Aporte.")

        aporte.validar_valor()
        self.aportes.append(aporte)
        self.verificar_status()

    def calcular_valor_restante(self):
        return max(
            0,
            self.valorObjetivo - self.calcular_valor_atual()
        )

    def verificar_status(self):
        if self.calcular_valor_atual() >= self.valorObjetivo:
            self.status = "Concluída"
        else:
            self.status = "Em andamento"

        return self.status
    
    def calcular_valor_projetado(self, estrategia: EstrategiaCrescimento) -> float:
        valor_atual = self.calcular_valor_atual()
        return estrategia.calcular(valor_atual)

    
    def calcular_valor_com_regra(self, regra: RegraDeRendimento) -> float:
        if not isinstance(regra, RegraDeRendimento):
            raise TypeError("É necessário fornecer uma RegraDeRendimento.")

        valor_atual = self.calcular_valor_atual()
        return regra.calcular_rendimento(valor_atual)

    
    def calcular_aporte_liquido(
        self,
        aporte: Aporte,
        estrategia: EstrategiaTaxa
    ) -> float:
        if not isinstance(aporte, Aporte):
            raise TypeError("É necessário fornecer um objeto Aporte.")

        if not isinstance(estrategia, EstrategiaTaxa):
            raise TypeError("É necessário fornecer uma estratégia de taxa.")

        aporte.validar_valor()

        return estrategia.calcular(aporte.valor)



