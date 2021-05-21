# Lista é uma variável composta assim como as tuplas, porém com algumas diferenças, vamos ver as caracteristicas de uma lista em python:

# Ao invés de serem representadas com (), são representadas com []

lista = [1,2,3,4]
print(lista)

# Para criar uma lista vazia, faça:

vazia_um = []

# ou

vazia_dois = list()

# As listas podem ser modificadas:

lista[3] = 5
print(lista)

# Para adicionar um novo elemento na lista, eu preciso usar o seguinte comando:

lista.append(6) #Vai adicionar o 6 no final da lista
print(lista)

# Para adicionar um novo elemento em qualquer lugar da lista, utilizo o seguinte comando:

lista.insert(0, 4) # 0 é a posição que vou inserir o 4, aqui ele irá empurar minha lista para frente.
print(lista)

# Para apagar um item da lista, use o comando abaixo:

del lista[3] # Excluir o elemento da posição 3

# ou

lista.pop(3) # Excluir o elemento da posição 3, se eu não colocar a posição ele apaga o ultimo elemento

print(lista)

# Podemos eliminar também pelo valor da posição com o comando:

# Parei aqui
#-------------------------------------------------

lista.remove(4) # Vai remover o VALOR 4 que está na posição 0, mas só remove a primeira ocorrência do valor 4.
print(lista)

# SE você remover um valor ou posição que não existe na lista, você irá recber um erro do Pytho, mas para mitigar esse erro, podemos utilizar o IF e o operador IN para verificar se o elemento existe na lista antes de remover:

if 4 in lista: # Se o 4 estiver dentro(in) da lista, faça...
   lista.remove(4)
   print(lista)
else:
   print('Esse elemento não existe na lista')

# Podemos criar uma lista a partir de outro comando, o range:

lista_dois = list(range(4, 11)) # Cria uma lista com numeros de 4 até 10
print(lista_dois)

# Para colocar os itens de uma lista em ordem crescente, utilize o seguinte comando:

crescente = [3,6,2,8,4,9]
crescente.sort()
print(crescente)

# Para colocar em ordem decrescente, utilize:

crescente.reverse()
print(crescente)

#Para saber o tamanho de uma lista, use: 

print(len(crescente))

#Ligação de listas:

a = [3,5,7]
b = a #Esse comando liga as listas, então tudo o que eu modificar em uma será modificado em outra

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Cópia de listas:

a = [3,5,7]
b = a[:] #Esse comando copia todos os elementos da lista a para a b

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Exemplos extras:

for position, c in enumerate(lista): #Mostrar a posição e o valor da lista
   print(f'A posição de {c} é {position}', end = '-')
    # end='' substitui o \n implicito do print, colocando todos os elementos na mesma linha, seguido de algum caractere

