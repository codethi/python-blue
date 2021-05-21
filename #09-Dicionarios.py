# Até agora vimos dois tipos de variáveis compostas, as tuplas e as listas, agora vamos ver a terceira, que são os dicionários.

# Na aula passada vimos que as listas podem ser representadas dessa forma:

lista = list()
lista.append('Thiago')
lista.append(27)

# Se eu quiser mostrar o nome eu tenho que dar esse print:

print(lista[0]) # Vai mostrar: Thiago

# Se eu quiser mostrar a idade:

print(lista[1]) # Vai mostrar 27

# Então para acessar os dados da minha lista, eu preciso indicar sempre os indices ou posições em que esse dado esta.

# Mas e se eu quisesse acessar o nome por um indice literal(palavras)? Como por exemplo:

# print(lista[nome]) Mostra os dados da "posição" nome.

# Isso não existe em listas, por isso temos os dicionários.

# A gente viu que as tuplas são representadas por (parenteses), as listas por [colchetes] já os dicionários são representados por {chaves}

# Existem duas opções para declarar um dicionário:

dados = dict()
dados = {'nome': 'Thiago', 'idade': 27} # Agora o meu "indice" para o nome é: nome.

# Agora sim o print que tentamos ali em cima vai dar certo(print(lista[nome])), porém faltou as aspas, a gente chama o dado assim:

print(dados['nome']) # Mostra os dados do indice nome (não esqueça as aspas).
print(f'O nome é: {dados["nome"]}') # Precisamos colocar aspas duplas dentro dos colchetos pois o dado já está entre aspas simples, por causa da f string.

# Para adicionar mais um indice e um dado, o append() não funciona, nós podemos simplemente escrever:

dados['sexo'] = 'M' # Ele não vai achar esse indice 'sexo' no dicionário, então ele vai inserir uma nova posição e adicionar o valor 'M'

print(dados)

# Para remover os dados, podemos usar o seguinte código:

del dados['idade'] # Vai remover o indice 'idade' com todos os dados dele.

print(dados)

# Se tentarmos acessar alguma chave que não existe, precisamos utilizar a função get()

print(dados['altura']) # Isso vai dar o erro KeyError


# Podemos validar isso com o get() e um if

if dados.get('altura') == None:
   print('Não existe altura para essa pessoa')
else:
   print('Altura existe')

# Para solucionar de uma forma ainda melhor, em Python você consegue atribuir uma valor padrão a uma key inexistente, com a função setdefault():

if dados.get('altura') == None:
   dados.setdefault('altura', 1.70) # Cria a chave altura e adiciona o valor 1.70.
   print('Altura inserida, com sucesso!')
else:
   print(dados['altura'])
print(dados)

# Importante caso a chave já exista e eu não coloquei esse setdefault() em um if, ele não faz nada, ou seja, ele não altera o valor pré adicionado!

#---------------------------------------------------------------------------------------

# Nos dicionários em Python nós temos os VALUE, KEYS e ITEMS.

# Os values são os valores do meu dicionário
# As keys são os indices.
# Os items são os dois juntos.

# Vamos ao exemplo de uma música:

musica = {
   'nome': 'Leave the Door Open',
   'autor': 'Bruno Mars',
   'lancamento': 2021
}

print(musica.values()) # Mostra apenas os valores dos indices
print(musica.keys()) # Mostra apenas os indices
print(musica.items()) # Mostra os indices e os valores.

# Podemos usar essas funções em um for, por exemplo:

for k in musica.keys(): # k = keys, função keys() mostra os indices ou chaves.
   print(k)

for v in musica.values(): # v = values, função values() mostra os valores ou dados.
   print(v)

for k, v in musica.items(): # k = keys, v = values, função items() mostra os dois.
   print(f'O {k} é {v}')

# Nós podemos juntar os conceitos de tupla, lista e dicionário no mesmo lugar.

# Por exemplo, se criarmos uma lista que receba vários dicionarios:

musica_um = {
   'nome': 'Leave the Door Open',
   'autor': 'Bruno Mars',
   'lancamento': 2021
}

musica_dois = {
   'nome': 'Empire state of mind',
   'autor': 'Alicia Keys',
   'lancamento': 2009
}

musica_tres = {
   'nome': 'Paradise',
   'autor': 'Coldplay',
   'lancamento': 2011
}

deezer = list()

deezer.append(musica_um)
deezer.append(musica_dois)
deezer.append(musica_tres)

print(deezer)
print(deezer[2]['autor'])
print(deezer[0]['nome'])
print(deezer[1]['lancamento'])

# Vamos a outro exemplo, adicionando os dados do dicionário com interação do usuário, através de um for:

pessoa = dict()
povo = list()

for c in range(0,3):
   pessoa['nome'] = str(input("Digite o nome: "))
   pessoa['idade'] = str(input('Digite a idade: '))
   povo.append(pessoa.copy()) # Se eu não colocar o copy() ele vai criar uma ligação.
print(povo)

# IMPORTANTE, o fatiamento [:] não funciona para dicionários

# Podemos deixar esse print mais bonitinho utilizando for aninhado a outro:

for p in povo: # Varre a lista povo que contem os dicionário pessoa.
   for v in p.values(): # Varre cada dicionário e mostra apenas os valores.
      print(v, end = ' ')
   print()

# Exercícios de exemplo:

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
   aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
   aluno['situacao'] = 'Recuperação'
else:
   aluno['situacao'] = 'Reprovado'
print()
for k, v in aluno.items():
   print(f'{k} é igual a {v}')

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter # Pega um item do dicionário por indice numerico

jogo = {
   'jogador1': randint(1,6),
   'jogador2': randint(1,6),
   'jogador3': randint(1,6),
   'jogador4': randint(1,6),
}

ranking = dict()

print('Valores sorteados: ')
for k, v in jogo.items():
   print(f'{k} tirou {v} no dado')
   sleep(1)

# Criação de um novo dicionário para ordenação:
   # sorted() ordenação
   # jogo.items(), o que eu quero ordenar, nesse caso as keys e values do dict jogo.
   # key=itemgetter(1), ordena apenas o indice 1(values do dict)
   # reverse = True, ordena em ordem reversa, para o maior ficar em primeiro
# Esse comando vai transformar meu dict em uma list:
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Agora para tratar esses dados, vamos precisar utilizar o enumerate:
print('-=' * 15)
print('Ranking de vencedores: ')
for i, v in enumerate(ranking):
   print(f'{i+1}° lugar: {v[0]} com {v[1]}')
   sleep(1)

# ----------------------------------------------------------------------------


