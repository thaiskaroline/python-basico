#LISTAS

#ANTES

nota1 = 9.9
nota2 = 8.5
nota3 = 5.8

#COM LISTAS
notas = [7.9, 8.5, 5.8]


#CRIANDO  LISTAS

lista = []
lista = list()
lista = [8,6,3, "Thais", True, 3.1415]
lista_de_listas = [10, [ 1,2,6]]

#INDEXAÇÃO E SLICES (FATIAMENTO)

#INDEXAÇÃO
lista = [8,6,3, "Thais", True, 3.1415]

print(lista[3]) #COMEÇANDO EM 0 ZERO PEGOU O ITEM 3 DA LISTA


#SLICES
lista = [1,2,3,4,5,6,7,8,50,62,32]

print(lista[0:3])#começa no zero e vai até o 3


#INTERAÇÕES COM FOR

#UTILIZANDO PROPRIOS ELEMENTOS DA LIST

for elemento in lista:#PRA CADA ELEMENTO DENTRO DA LISTA
    print(elemento)
    
#UTILIZANDO INDICES

print('comprimento da lista',len(lista)) #QUANTIDADE DE ELEMENTOS DA LISTA
    
    
for i in range(len(lista)):
    print(lista(i))