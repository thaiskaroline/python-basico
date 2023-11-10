#METODOS DE LISTA

lista = [1, 3, 12, 8,2]

#append
#ADICIONAR NO FINAL
print(lista)

print("Antes do append: ", lista)
lista.append(3)


print("Depois do append: ", lista)


#insert
#ESCOLHE QUAL A POSIÇÃO QUE VOCÊ QUER ADICIONAR O ELEMENTO

lista.insert(2, 15)

print("Depois do Insert: ", lista)


#extend

#JUNTAR DUAS LISTAS COLOCANDO NO FINAL

lista2 = [1,2,3]

lista.extend(lista2)

print("Depois do extend: ", lista)


#pop

#REMOVER ELEMENTO ESPECIFICADO
#QUANDO NÃO É PASSADO PARAMETRO ELE REMOVE O ULTIMO ELEMENTO

lista.pop()

print("Depois do pop: ", lista)

lista.pop(0) #ESPECIFICANDO INDICE QUE QUER REMOVER

print("Depois do pop: ", lista)

#remove
#VOCÊ ESPECIFICA O ELEMENTO E NÃO O INDICE QUE QUER REMOVER
#REMOVE O PRIMEIRO ELEMENTO ENCONTRADO

lista.remove(3)

print("Depois do remove: ", lista)


#count

print("Quantidade de 2 na lista", lista.count(2))


#index
#EXIBE O ELEMENTO INDICADO PELO INDICE

print("Indice do elemento 12: ", lista.index(12))

#sort
#ORDENA A LISTA
lista.sort()

print(lista)

lista.sort(reverse=True) #INVERTE A ORDEM DA LISTA


print(lista)


#FUNÇÕES

#len
#retorna a quantidade de elementos da lista

print(len(lista))

#sum
#soma todos os valores da lista
total = sum(lista)
print(sum(lista))

#max
#encontra o maior valor da lista
maior_valor = max(lista) #NÃO É NECESSÁRIO
print("Maior elemento da lista", max(lista))

#min
#encontra o menor valor da lista
menor_valor = min(lista)#NÃO É NECESSÁRIO
print("Menor elemento da lista", min(lista))

