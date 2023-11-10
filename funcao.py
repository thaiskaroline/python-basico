#FUNÇÕES

#FUNÇÕES UTILIZADAS


"""print() #IMPRIMI MENSAGEM (INT, FLOAR, STR) NO CONSOLE (TERMINAL)
input() #RETORNA UM DADO INFORMADO PELO USUÁRIO (ENTRADA PADRÃO)
len() # RECEBE UMA LISTA E RETORNA O TAMANHO DESSA LISTA
max() # RETORNA O MAIOR VALOR DE UMA LISTA
"""

#CRIAÇÃO DE FUNÇÕES

#FUNÇÃO INICIAL

def saudacao():
    print("Bem vindo ao nosso programa!")
    print("Olá, é um prazer ter você neste curso")
    
    
saudacao()
saudacao()
saudacao()

#FUNÇÃO COM PARAMETROS

def saudacao(nome, curso):
    print(f"Bem vindo, {nome} ao nosso programa!")
    print(f"Olá, é um prazer ter você neste curso de {curso}")
    
    
saudacao("Thais", "Engenharia de dados")
saudacao("Vinicius", "Python")

#FUNÇÕES COM PARAMETRO DEFAULT

def saudacao(nome, curso="Python"):
    print(f"Bem vindo, {nome} ao nosso programa!")
    print(f"Olá, é um prazer ter você neste curso de {curso}")
    
saudacao("Thais")
saudacao("Vinicius", "C++")

#FUNÇÕES COM RETORNO


def soma(num1, num2):
    #print("soma = ", num1 + num2)
    return num1 + num2
    
resultado = soma(5, 8)

print("O resultado da soma é ", resultado)

def calculadora (num1, num2, operacao ="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    
    
resultado = calculadora(10, 20)
print(resultado)