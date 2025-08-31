from Transacao import Transacao
from Conta import Conta
class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
        self.mensagem = f"Depósito de {valor}"

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)
        print(self.mensagem)