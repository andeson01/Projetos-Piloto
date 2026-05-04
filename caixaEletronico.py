def imprimirComprovante():
    resposta = input("Deseja imprimir o comprovante? (S/N): ").upper()
    if resposta == "S":
        print("Imprimindo comprovante...\n")
    elif resposta == "N":
        print("Operação realizada sem comprovante.\n")
    else:
        print("Comando não reconhecido.\n")

def consultarValor():
    print(f"\n---- SALDO DISPONÍVEL: R${saldoDisponivel:.2f} ----")

def sacarValor():
    global saldoDisponivel
    try:
        valorSaque = float(input("DIGITE O VALOR QUE DESEJA SACAR: "))
        if valorSaque <= saldoDisponivel:
            saldoDisponivel -= valorSaque
            print(f"\nSaque de R${valorSaque:.2f} realizado com sucesso!\n")
            imprimirComprovante()
        else:
            print("SALDO INSUFICIENTE!\n")
    except ValueError:
        print("ERRO: Digite um valor numérico válido para o saque.\n")

def transferirValor():
    global saldoDisponivel
    nomePessoa = input("\nDIGITE O NOME DE QUEM VOCÊ VAI TRANSFERIR: ")
    
    try:
        valorTransferencia = float(input("DIGITE O VALOR QUE DESEJA TRANSFERIR: "))
        
        if valorTransferencia <= saldoDisponivel:
            saldoDisponivel -= valorTransferencia
            print(f"\nTransferência para {nomePessoa} no valor de R${valorTransferencia:.2f} realizada!\n")
            imprimirComprovante()
        else:
            print("SALDO INSUFICIENTE PARA TRANSFERÊNCIA!\n")
    except ValueError:
        print("ERRO: Digite um valor numérico válido para a transferência.\n\n")

def depositarValor ():
    global saldoDisponivel
    valorDeposito = float(input("DIGITE O VALOR QUE VOCÊ VAI DEPOSITAR: "))
    saldoDisponivel = valorDeposito + saldoDisponivel
    print(f"Depósito de R${valorDeposito} realizado com sucesso")

# --- PROGRAMA PRINCIPAL ---
saldoDisponivel = 5000

while True:
    print("""
            OPERAÇÕES
        1 - CONSULTAR SALDO
        2 - SACAR VALOR
        3 - TRANSFERIR VALOR
        4 - DEPOSITAR VALOR
        5 - SAIR
    """)
    
    try:
        opcaoDigitada = int(input("DIGITE A OPÇÃO DESEJADA: "))

        if opcaoDigitada == 1:
            consultarValor()
        elif opcaoDigitada == 2:
            sacarValor()
        elif opcaoDigitada == 3:
            transferirValor()
        elif opcaoDigitada == 4:
            depositarValor()
        elif opcaoDigitada == 5:
            confirmar = input("DESEJA REALMENTE SAIR? (S/N): ").upper()
            if confirmar == "S":
                print("ENCERRANDO SISTEMA... ATÉ LOGO!")
                break
        else:
            print("""
                  
                  OPÇÃO INVÁLIDA!
                  
                  """)
            
    except ValueError:
        print("ERRO: Digite apenas o número da opção (1, 2, 3, 4 ou 5).")