menu = """
=======MENU=======
    [1] - Sacar
    [2] - Depositar
    [3] - Extrato
    [4] - Sair
==================
"""

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        saque = float(input("Digite o valor a ser sacado \n>>"))
        
        excedeu_saldo = saque > saldo 
        excedeu_limite = saque > limite
        excedeu_saques = quantidade_saques > limite_saques

        if excedeu_saldo:
            print("Inválido, saldo excedido !!!")
        elif excedeu_limite:
            print("Inválido, limite excedido !!!")
        elif excedeu_saques:
            print("Inválido, limite de saques excedidos, máximo 3 !!!")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque igual: {saque:.2f}\n"
            quantidade_saques += 1

    elif opcao == "2":
        valor = float(input("Digite o valor depositado \n>>"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito igual: {valor:.2f}\n"
        else:
            print("Valor inválido, tente novamente")

    elif opcao == "3":
        print("\n=======EXTRATO=======")
        print("Não foram feitas movimentações bancárias" if not extrato else extrato)
        print(f"\nSaldo:R$ {saldo:.2f}")
        print("=====================")

    elif opcao == "4":
        break

    else:
        print("Opção inválida, digite novamente")
