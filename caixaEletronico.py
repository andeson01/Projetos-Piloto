def imprimirComprovante(resposta):
    if resposta == "S":
        print("Imprimindo comprovante...\n")
        
    elif resposta == "N":
        print("Saque realizado sem comprovante.\n")
    else:
        print("Comando não reconhecido.\n")


saldoDisponivel = 3000
while True:
    valorSaque = float(input(f"Saldo disponível: R${saldoDisponivel}\nQuanto você vai sacar?\n"))

    if valorSaque > 0 and valorSaque <= saldoDisponivel:
        print("Saque aprovado\n")
        saldoDisponivel -= valorSaque #atualiza o valor
        escolha = input("Deseja imprimir o comprovante (S/N) ?\n").upper()
        imprimirComprovante(escolha)
    else:
        print("Saque negado.\n")

    comando = int(input("Digite 1 para continuar e 0 para parar a execução\n"))
    if comando == 0:
        print(f"Sobrou R${saldoDisponivel}, encerrando o sistema. Até logo!")
        break