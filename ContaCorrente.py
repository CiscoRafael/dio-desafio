from Conta import Conta
from Historico import Historico
from Cliente import Cliente
class ContaCorrente (Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, limite: float, limite_saques: int):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite 
        self.limite_saques = limite_saques
        self.saques_realizados = 0
        
    def sacar(self, valor: float) -> bool:
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques atingido")
            return False
        if valor > self.limite:
            print("Valor acima do limite da conta")
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        else:
            print("Saldo insuficiente")
            return False