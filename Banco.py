from datetime import date
from Cliente import Cliente
from ContaCorrente import ContaCorrente
from Deposito import Deposito
from Saque import Saque
        
def main():
    clientes = []
    contas = []

    while True:
        print("\n=== Menu Principal ===")
        print("1 - Criar Usuário")
        print("2 - Criar Conta Corrente")
        print("3 - Entrar na conta")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("Digite o CPF: ")
            nome = input("Digite o nome: ")
            data_nasc = input("Digite a data de nascimento (DD-MM-AAAA): ")
            ano, mes, dia = map(int, data_nasc.split('-'))
            endereco = input("Digite o endereço: ")
            cliente = Cliente(cpf, nome, date(dia, mes, ano), endereco)
            clientes.append(cliente)
            print(f"Usuário {nome} criado com sucesso!")

        elif opcao == "2":
            if not clientes:
                print("Nenhum usuário cadastrado. Crie um usuário primeiro.")
                continue
            print("Usuários cadastrados:")
            for i, c in enumerate(clientes):
                print(f"{i+1} - {c.nome}")
            idx = int(input("Escolha o usuário para criar a conta: ")) - 1
            if 0 <= idx < len(clientes):
                cliente = clientes[idx]
                numero = int(input("Digite o número da conta: "))
                limite = float(input("Digite o limite da conta: "))
                limite_saques = int(input("Digite o limite de saques: "))
                conta = ContaCorrente(0.0, numero, "0001", cliente, limite, limite_saques)
                cliente.adicionar_conta(conta)
                contas.append(conta)
                print(f"Conta corrente {numero} criada para {cliente.nome}!")
            else:
                print("Usuário inválido.")

        elif opcao == "3":
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue
            numero = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c.numero == numero), None)
            if conta is None:
                print("Conta não encontrada.")
                continue
            
            while True:
                print(f"\n=== Menu Conta {conta.numero} ===")
                print("1 - Depositar")
                print("2 - Sacar")
                print("3 - Ver Extrato")
                print("4 - Voltar")
                subopcao = input("Escolha uma opção: ")

                if subopcao == "1":
                    valor = float(input("Digite o valor do depósito: "))
                    deposito = Deposito(valor)
                    deposito.registrar(conta)

                elif subopcao == "2":
                    valor = float(input("Digite o valor do saque: "))
                    saque = Saque(valor)
                    saque.registrar(conta)

                elif subopcao == "3":
                    print("\n--- Extrato ---")
                    for t in conta.historico.transacoes:
                        print(f"{t.__class__.__name__}: {t.valor}")
                    print(f"Saldo atual: {conta.saldo}")

                elif subopcao == "4":
                    break

                else:
                    print("Opção inválida.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

main()