from Transacao import Transacao
from Conta import Conta
class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
        self.mensagem = f"Saque de {valor}"

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            print(self.mensagem)
        else:
            print("Saldo insuficiente")