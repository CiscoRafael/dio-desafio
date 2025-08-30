class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco  
        
        
class Conta:
    contador_contas = 1
    def __init__(self, usuario : Usuario):
        self.agencia = "0001"
        self.numero_conta = Conta.contador_contas
        Conta.contador_contas += 1
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
    
    def depositar(self, valor: float, conta : Conta):
        conta.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        conta.extrato += f"Depósito: R$ {valor:.2f}\n"

    def sacar(self, valor: float, conta : Conta):
        if conta.saldo >= valor:
            conta.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            conta.extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print(f"Saldo insuficiente. Saldo atual: R$ {conta.saldo:.2f}")

    def ver_extrato(self, conta : Conta):
        print("================ EXTRATO ================")
        
        if conta.extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(conta.extrato)
            
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        print("=========================================")
        
    def criar_usuario(self):
        nome = input("Digite o nome do usuario: ")
        data_nascimento = ("Digite a data de nascimento no formato (dd/mm/aaaa): ")
        cpf = input("Digite o CPF (11 números): ")
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido! Digite exatamente 11 números.")
            return
        cpf_str = str(cpf)
        cpf_str = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        endereco = input("Informe o endereço no formato (Logradouro - Bairro - Cidade - Sigla Estado): ")
        
        usuario = Usuario(nome, data_nascimento, cpf_str, endereco)
        self.usuarios.append(usuario)
        print("Usuário criado com sucesso!")
        
    def criar_conta_corrente(self, cpf_usuario):
        cpf_str = f"{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}"
        for usuario in self.usuarios:
            if usuario.cpf == cpf_str:
                conta_corrente = Conta(usuario)
                print(f"Conta criada com sucesso! Agência: {conta_corrente.agencia}, Número: {conta_corrente.numero_conta}")
                return conta_corrente
        else:
            print("Usuario não cadastrado")
            return None
        
def main():
    banco = Banco()
    conta_atual = None

    while True:
        print("\n=== Menu ===")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Ver Extrato")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            banco.criar_usuario()
        
        elif escolha == '2':
            cpf = input("Informe o CPF do usuário: ")
            conta_atual = banco.criar_conta_corrente(cpf)
        
        elif escolha == '3':
            if conta_atual:
                valor = float(input("Digite o valor a ser depositado: "))
                banco.depositar(valor, conta_atual)
            else:
                print("Nenhuma conta selecionada. Crie uma conta primeiro.")
        
        elif escolha == '4':
            if conta_atual:
                valor = float(input("Digite o valor a ser sacado: "))
                banco.sacar(valor, conta_atual)
            else:
                print("Nenhuma conta selecionada. Crie uma conta primeiro.")
        
        elif escolha == '5':
            if conta_atual:
                banco.ver_extrato(conta_atual)
            else:
                print("Nenhuma conta selecionada. Crie uma conta primeiro.")
        
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()