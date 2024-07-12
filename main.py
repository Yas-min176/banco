class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def consultar_extrato(self):
        print("Extrato:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

def menu():
    conta = None
    
    while True:
        print("\n=== Menu Banco ===")
        if conta:
            print("1. Depositar")
            print("2. Sacar")
            print("3. Consultar saldo")
            print("4. Consultar extrato")
            print("5. Sair")
        else:
            print("1. Criar conta")
            print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1" and not conta:
            titular = input("Informe o nome do titular da conta: ")
            saldo_inicial = float(input("Informe o saldo inicial da conta: "))
            conta = ContaBancaria(titular, saldo_inicial)
            print(f"Conta criada com sucesso para {titular} com saldo inicial de R${saldo_inicial:.2f}.")
        
        elif opcao == "1" and conta:
            valor = float(input("Informe o valor para depósito: "))
            conta.depositar(valor)
        
        elif opcao == "2" and conta:
            valor = float(input("Informe o valor para saque: "))
            conta.sacar(valor)
        
        elif opcao == "3" and conta:
            conta.consultar_saldo()
        
        elif opcao == "4" and conta:
            conta.consultar_extrato()
        
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida ou indisponível. Tente novamente.")

menu()