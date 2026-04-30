reta1 = float(input("Digite quanto vale a primeira reta do triângulo: "))
reta2 = float(input("Digite quanto vale a segunda reta do triângulo: "))
reta3 = float(input("Digite quanto vale a terceira reta do triângulo: "))

print(" ") #apenas para separar as e/s

if reta1 == reta2 == reta3:
    print("O triângulo é EQUILÁTERO")

elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print("O triângulo é ISÓSCELES")

else:
    print("O triângulo é ESCALENO")