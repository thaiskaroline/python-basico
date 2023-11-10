#DICIONARIOS

#CRIANDO DICIONARIOS

dicionario = {}
dicionario= dict()

dicionario = {"nome" : "Thais", "idade": 23, "altura": 1.64}

print(dicionario)

print(dicionario["idade"])

#ADICIONANDO ELEMENTOS EM UM DICIONARIO

dicionario["programador"] = True

print(dicionario)

dicionario["altura"] = 2

print(dicionario)

#PERCORRENDO VALORES DO DICIONARIO

for chave in dicionario:
    print(chave, dicionario[chave])
    
    
#TESTANDO A EXISTENCIA DE UMA CHAVE

print("peso" in dicionario)
print("altura" in dicionario)