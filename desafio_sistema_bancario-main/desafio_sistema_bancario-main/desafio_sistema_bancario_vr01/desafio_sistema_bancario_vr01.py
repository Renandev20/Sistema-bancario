menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

continuar = True

while continuar:
    
    print(f"""
         ==========  Obrigado por utilizar nosso banco!  ==========
         
          \033[1mEscolha no Menu a operação desejada:\033[0m
          """)

    opcao = input(menu.center(24,"#"))

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("\033[1mObrigado por utilizar nossos serviços, volte sempre\033[0")
        continuar = False

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
    if opcao != "0":
        resposta = input("Deseja realizar outra operação? (s/n): ")
        if resposta.lower() == 'n':
            print("\033[1mObrigado por utilizar nossos serviços, volte sempre\033[0")
            continuar = False