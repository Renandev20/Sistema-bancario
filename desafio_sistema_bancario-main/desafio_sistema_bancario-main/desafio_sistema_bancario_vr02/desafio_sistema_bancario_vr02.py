import textwrap

# Constantes para limites e agência
LIMITE_SAQUES = 3
AGENCIA = "0001"

# Função para exibir o menu
def menu():
    menu_text = """\n
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Exibir extrato
    [4] Criar novo usuário
    [5] Criar nova conta
    [6] Listar usuários
    [7] Listar contas
    [8] Modificar usuário
    [0] Sair
    => """
    try:
        return int(input(textwrap.dedent(menu_text)))
    except ValueError:
        return -1  # Retorna um valor fora das opções válidas

# Função para filtrar usuários por CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar um novo usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }
    usuarios.append(novo_usuario)

    print("\n=== Usuário criado com sucesso! ===")
    return novo_usuario

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")

# Função para modificar as informações de um usuário
def modificar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário a ser modificado: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado. Não foi possível modificar. @@@")
        return

    print("\n=== Modificando usuário ===")
    usuario["nome"] = input("Informe o novo nome completo: ")
    usuario["data_nascimento"] = input("Informe a nova data de nascimento (dd-mm-aaaa): ")
    usuario["endereco"] = input("Informe o novo endereço (logradouro, número - bairro - cidade/estado): ")

    print("\n=== Usuário modificado com sucesso! ===")

# Função para realizar um depósito
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o saldo e o extrato após o depósito
    return saldo, extrato

# Função para realizar um saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    # Retorna o saldo e o extrato após o saque
    return saldo, extrato


# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Função para criar uma nova conta
def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado. Criação de conta encerrada! @@@")
        return None

    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0,
        "limite_saques": LIMITE_SAQUES,
    }

    contas.append(nova_conta)
    print("\n=== Conta criada com sucesso! ===")
    return nova_conta

# Função para listar todas as contas
def listar_contas(contas):
    if len(contas) == 0:
        print("\nNenhuma conta cadastrada.")
        return

    for conta in contas:
        usuario = conta["usuario"]
        linha = f"""\
            Agência:\t{conta["agencia"]}
            Conta:\t\t{conta["numero_conta"]}
            Titular:\t{usuario["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal para controlar o fluxo do menu
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            # Atualiza saldo e extrato com o retorno do depósito
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            # Atualiza saldo e extrato com o retorno do saque
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            criar_conta(AGENCIA, contas, usuarios)

        elif opcao == 6:
            listar_usuarios(usuarios)

        elif opcao == 7:
            listar_contas(contas)

        elif opcao == 8:
            modificar_usuario(usuarios)

        elif opcao == 0:
            print("\nObrigado por utilizar nossos serviços! Até logo!")
            break

        else:
            print("\nOpção inválida. Por favor, tente novamente.")


# Executar a função principal
main()
