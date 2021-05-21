#É uma variável que guarda de 1 a N valores, ou seja, ela vai criar vários espaços na memória para você e irá guarda em apenas 1 variável.

#Para acessar os elementos dentro da tupla a gente utiliza os indices, assim como na String, o indice sempre inicia no zero.

alunos = ('José', 'Maria', 'Augusto', 'Mayara') #Tupla são representadas por parenteses, nas ultimas atualizações, nem precisa de parenteses

print(alunos)

print(alunos[2])

print(alunos[0:2])

print(alunos[1:])

print(len(alunos))

print(sorted(alunos)) #não altera a tupla, apenas ordena.

#AS TUPLAS SÃO IMUTÁVEIS

alunos[0] = 'Thiago' #Isso não funciona, porque eu não consigo atribuir itens a tuplas a não ser na atribuição dela.

#Nós conseguimos concatenar tuplas também:

a = (1, 2 ,3)
b = (4, 5, 6, 7, 8)
c = a + b
print(c)

print(len(c))

print(c.count(3)) #conta quantas vezes o 3 aparece.

print(c.index(7)) #mostra a posição do 7 na tupla. Aqui ele pega a primeira ocorrencia do numero na tupla.

#As tuplas podem receber valores de tipos diferentes:

pessoa = ('Thiago', 27, 'Casado', 1.70, True)
print(pessoa)

del(pessoa) #Apaga toda a tupla, porem você não pode deletar apenas um item da tupla

