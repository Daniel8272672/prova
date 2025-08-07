cadastro = input("Bem-vindo ao DaniBank! Digite seu nome para realizar o cadastro: ")
saldo = 0.0
opcao = "" 

print(f"\nOlá, {cadastro}! Sua conta foi criada com saldo inicial de R$ {saldo:.2f}\n")

while opcao != "sair":
    print("\n--- Menu ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Listar saldo")
    print("sair")

    opcao = input("Escolha uma opção (1-3 ou sair): ")

    match opcao:
        case "1":
            valor = float(input("Digite um valor para depositar: R$ "))
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        case "2":
            valor = float(input("Digite o valor para sacar: R$ "))
            if valor > saldo:
                print("Saldo insuficiente para essa operação.")
            else:
                saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        case "3":
            print(f"Saldo atual: R$ {saldo:.2f}")

        case "sair":
            print(f"\nObrigado por usar o DaniBank, {cadastro}. Até breve!")

        case _:
            print("Opção inválida. Tente novamente.")
