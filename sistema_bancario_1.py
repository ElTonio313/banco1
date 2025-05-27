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
#quantidade_saques = 0
#limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        saque = float(input("Digite o valor a ser sacado \n>>"))
        if saque < limite and saque <= saldo:
            saldo -= saque
            extrato += f"Saque igual: {saque:.2f}\n"
        else:
            print("Valor inválido, tente novamente")

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