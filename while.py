numero_secreto = 3

numero = int(input("DIGITE UM NUMERO: "))



while numero != numero_secreto:
    print("Errado, tente novamente.")
    numero = int(input("DIGITE UM NUMERO: "))
    
print("Você acertou")


#EXEMPLO COM CONTADOR

contador = 0

while contador < 5:
    print(contador)
    
    contador = contador + 1