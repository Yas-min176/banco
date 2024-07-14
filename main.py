from abc import ABC, abstractmethod

class ContaBancaria:
    contador_contas = 0

    def __init__(self, titular, saldo=0, limite=0, limite_saque=0):
        ContaBancaria.contador_contas += 1
        self.numero_conta = ContaBancaria.contador_contas
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.limite_saque = limite_saque
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0:
            limite_total = self.saldo + self.limite
            if valor <= limite_total and valor <= self.limite_saque:
                self.saldo -= valor
                self.extrato.append(f"Saque: R${valor:.2f}")
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Valor de saque excede o limite disponível.")
        else:
            print("Valor de saque inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Limite disponível: R${self.limite:.2f}")
        print(f"Limite de saque disponível: R${self.limite_saque:.2f}")

    def consultar_extrato(self):
        print("Extrato:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Limite disponível: R${self.limite:.2f}")
        print(f"Limite de saque disponível: R${self.limite_saque:.2f}")

class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def criar_conta(self, saldo_inicial=0, limite=0, limite_saque=0):
        nova_conta = ContaBancaria(self.nome, saldo_inicial, limite, limite_saque)
        self.contas.append(nova_conta)
        print(f"Conta criada com sucesso para {self.nome}. Número da conta: {nova_conta.numero_conta}")
        return nova_conta

    def obter_contas(self):
        return self.contas

    def obter_endereco(self):
        return self.endereco

    def verificar_estado_contas(self):
        if not self.contas:
            print("Cliente não possui contas cadastradas.")
        else:
            print(f"Estado das contas para o cliente {self.nome}:")
            for conta in self.contas:
                print(f"Número da conta: {conta.numero_conta}")
                conta.consultar_saldo()
                print("")

class InterfaceBanco(ABC):
    @abstractmethod
    def criar_cliente(self):
        pass

    @abstractmethod
    def criar_conta(self, cliente):
        pass

    @abstractmethod
    def depositar(self, conta, valor):
        pass

    @abstractmethod
    def sacar(self, conta, valor):
        pass

    @abstractmethod
    def consultar_saldo(self, conta):
        pass

    @abstractmethod
    def consultar_extrato(self, conta):
        pass

    @abstractmethod
    def verificar_estado_contas(self, cliente):
        pass

class InterfaceBancoConsole(InterfaceBanco):
    def __init__(self):
        self.cliente = None

    def criar_cliente(self):
        if self.cliente:
            print("Cliente já cadastrado.")
        else:
            cpf = input("Informe o CPF do cliente: ")
            nome = input("Informe o nome do cliente: ")
            data_nascimento = input("Informe a data de nascimento do cliente (DD/MM/AAAA): ")
            endereco = input("Informe o endereço do cliente: ")
            self.cliente = Cliente(cpf, nome, data_nascimento, endereco)
            print(f"Cliente cadastrado com sucesso: {nome} (CPF: {cpf}), nascido em {data_nascimento}, morando em {endereco}.")

    def criar_conta(self, cliente):
        saldo_inicial = float(input("Informe o saldo inicial da conta: "))
        limite = float(input("Informe o limite da conta: "))
        limite_saque = float(input("Informe o limite de saque da conta: "))
        nova_conta = cliente.criar_conta(saldo_inicial, limite, limite_saque)

    def depositar(self, conta, valor):
        conta.depositar(valor)

    def sacar(self, conta, valor):
        conta.sacar(valor)

    def consultar_saldo(self, conta):
        conta.consultar_saldo()

    def consultar_extrato(self, conta):
        conta.consultar_extrato()

    def verificar_estado_contas(self, cliente):
        cliente.verificar_estado_contas()

def menu(interface):
    while True:
        print("\n=== Menu Banco ===")
        print("1. Criar cliente")
        print("2. Criar conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Consultar saldo")
        print("6. Consultar extrato")
        print("7. Verificar estado das contas")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            interface.criar_cliente()
        elif opcao == "2":
            if interface.cliente:
                interface.criar_conta(interface.cliente)
            else:
                print("Crie um cliente primeiro.")
        elif opcao == "3":
            if interface.cliente:
                conta_index = int(input("Informe o número da conta para depositar: ")) - 1
                if conta_index < len(interface.cliente.contas):
                    valor = float(input("Informe o valor para depósito: "))
                    interface.depositar(interface.cliente.contas[conta_index], valor)
                else:
                    print("Conta não encontrada.")
            else:
                print("Crie um cliente primeiro.")
        elif opcao == "4":
            if interface.cliente:
                conta_index = int(input("Informe o número da conta para sacar: ")) - 1
                if conta_index < len(interface.cliente.contas):
                    valor = float(input("Informe o valor para saque: "))
                    interface.sacar(interface.cliente.contas[conta_index], valor)
                else:
                    print("Conta não encontrada.")
            else:
                print("Crie um cliente primeiro.")
        elif opcao == "5":
            if interface.cliente:
                conta_index = int(input("Informe o número da conta para consultar saldo: ")) - 1
                if conta_index < len(interface.cliente.contas):
                    interface.consultar_saldo(interface.cliente.contas[conta_index])
                else:
                    print("Conta não encontrada.")
            else:
                print("Crie um cliente primeiro.")
        elif opcao == "6":
            if interface.cliente:
                conta_index = int(input("Informe o número da conta para consultar extrato: ")) - 1
                if conta_index < len(interface.cliente.contas):
                    interface.consultar_extrato(interface.cliente.contas[conta_index])
                else:
                    print("Conta não encontrada.")
            else:
                print("Crie um cliente primeiro.")
        elif opcao == "7":
            if interface.cliente:
                interface.verificar_estado_contas(interface.cliente)
            else:
                print("Crie um cliente primeiro.")
        elif opcao == "8":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

interface = InterfaceBancoConsole()
menu(interface)
