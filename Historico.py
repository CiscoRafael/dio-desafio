from Transacao import Transacao

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)
        print(f"Transação {transacao.__class__.__name__} registrada!")