velCarro = int(input("Digite a velocidade do carro (km/h): "))


print(f"""
      Sua velocidade é de {velCarro}km/h,
      ATENÇÃO PARA A MENSAGEM A SEGUIR:
      """)


if velCarro <= 80:
    print("Boa viagem! Dirija com segurança.")

elif velCarro > 80 and velCarro <= 100:
    print("Atenção: Você está acima do limite. Multa leve.")

elif velCarro > 100:
    print("PERIGO: Multa grave e retenção da carteira!")