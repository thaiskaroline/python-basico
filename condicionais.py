#ESTRUTURAS CONDICIONAIS

idade = int(input("Digite sua idade:  "))


if idade >= 18:
    print("Você é maior de idade")
else :
    print("Você é menor de idade")



nota1 = float(input("DIGITE A NOTA 1: "))
nota2 = float(input("DIGITE A NOTA 2: "))
nota3 = float(input("DIGITE A NOTA 3: "))
presenca = int(input("Digite a porcentagem de frequencia: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7 and presenca >= 100:
    print("APROVADO")
elif media >=5 and presenca >=50:
    print("RECUPERACAO")
else: 
    print("REPROVADO")