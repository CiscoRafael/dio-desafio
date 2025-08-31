from Historico import Historico
class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: "Cliente"):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        
    def saldo(self) -> float:
        return self.saldo
    
    @staticmethod
    def nova_conta(cliente: "Cliente", numero: int) -> "Conta":
        return Conta(0.0, numero, "0001", cliente)

    def sacar(self, valor: float) -> bool:
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    
    def depositar(self, valor: float) -> bool:
        self.saldo += valor
        return True