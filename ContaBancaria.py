class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = ""

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        self.extrato += f"Depósito: R$ {valor:.2f}\n"

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            self.extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}")

    def ver_extrato(self):
        print("================ EXTRATO ================")
        
        if self.extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(self.extrato)
            
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=========================================")


def main():
    conta = ContaBancaria()  # cria uma conta bancária

    while True:
        print("=== Menu ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif escolha == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif escolha == '3':
            conta.ver_extrato()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()