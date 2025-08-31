from datetime import date
from PessoaFisica import PessoaFisica
from Conta import Conta
from Transacao import Transacao
class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)