anoAtual = 2026
print("DESCUBRA SUA CATEGORIA")
anoNascimento = int(input("Digite o seu ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade > 0 and idade <= 9:
    print("Categoria: MIRIM")

elif idade > 9 and idade <= 14:
    print("Categoria: INFANTIL")

elif idade > 14 and idade <= 19:
    print("Categoria: JÚNIOR")

elif idade > 19 and idade <= 25:
    print("Categoria: SÊNIOR")

else:
    print("Categoria: MASTER")