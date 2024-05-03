menu = """
Bem vindo(a) ao banco X!

----- Menu de opções -----

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

------------------------------------

Escolha uma opção:

"""

saldo = 0
limite = 500
limite_saque = 3
numero_saque = 0
extrato = ""

while True:
    
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        
        else:
            print("Erro! O valor inserido é inválido.")


    elif opcao == "s":
        saque = float(input("Informe o quanto quer sacar: "))

        if numero_saque > limite_saque:
            print("Você excedeu o número máximo de saques hoje, tente novamente amanhã")
            break

        elif saque > 500:
            print(f"O limite de saques é de R$ {limite:.2f}")

        elif saque > saldo:
            print(f"Saldo insuficiente. Você tem R$ {saldo:.2f}")

        elif saque <= saldo:
            print("Saque realizado com sucesso, retire seu dinheiro!")
            saldo -= saque
            numero_saque += 1
            extrato += f"Saque: R$ {saque:.2f}\n"

        else:
            print("Operação inválida.")


    elif opcao == "e":
        print("\n--------- Extrato ---------\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo é de R$ {saldo:.2f}")
        print("\n----------- Fim -----------")

    elif opcao == "q":
        print("\nAgradecemos a preferência!")
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada.")
