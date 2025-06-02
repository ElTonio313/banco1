import textwrap

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito igual: {valor:.2f}\n"
    else:
        print("Valor inválido, tente novamente")
    return saldo, extrato
 
def sacar(*, saldo, saque, extrato, limite_saques, quantidade_saques, limite):
        
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
    else:
        print("Operação inválida")
    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
    print("\n=======EXTRATO=======")
    print("Não foram feitas movimentações bancárias" if not extrato else extrato)
    print(f"\nSaldo:R$ {saldo:.2f}")
    print("=====================")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=======Conta Criada com Sucesso=======\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    menu = """
=======MENU=======
    [1] - Sacar
    [2] - Depositar
    [3] - Extrato
    [4] - criar usuario
    [5] - criar contas
    [6] - listar contas
    [7] - Sair
==================
"""
    saldo = 0
    limite = 500
    extrato = ""
    quantidade_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"
    while True:
        opcao = input(menu)
        if opcao == "1":
            saque = float(input("Informe o Valor a ser sacado\n>> "))
            saldo, extrato = sacar(saque=saque, saldo=saldo, extrato=extrato,limite_saques=limite_saques, quantidade_saques=quantidade_saques, limite=limite) 

        elif opcao == "2":
            valor = float(input("Informe o valor do deposito\n>> "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Opção inválida")
main()
