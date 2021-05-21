# Funções são rotinas no meu programa.

#Rotinas são ações repetitivas, que posso sintetizar em uma função, para fazer repetidas vezes, sem ter que criar as mesmas linhas de código.

#Algumas funções que já vimos por aqui:

#ALTERAÇÕES QUE O THIAGO PEDIU
""" 
print()
input()
len()
int()
float() 
"""
# Alterações para dar ruim com o Vini
# Mas as vezes essas funções nativas não nos satisfazem...

def titulo():
   print('Sejam bem vindos ao meu programa!')


titulo()

#-------------------------------------------------------

# Parametro

def titulo(txt):
   print(txt)

titulo('Sejam bem vindos ao meu programa!')

#--------------------------------------------------------

#Outro exemplo

#Sem função
n1 = 5
n2 = 3
soma = n1 + n2
print(soma)

n1 = 1
n2 = 2
soma = n1 + n2
print(soma)

n1 = 7
n2 = 10
soma = n1 + n2
print(soma)

#Com função

def soma(n1, n2):
   soma = n1 + n2
   print(soma)

soma(5,3)
soma(1,2)
soma(7,10)

# Exercicios:

# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno:

def area(larg, comp):
   a = larg * comp
   print(f'A área de um terreno {larg} x {comp} é de {a}m²')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)


#--------------------------------------------------------

# comando HELP, é só digitar help(print) que ele mostra uma documentação da função

#Criando a documentação da minha função com DocStrings:

def soma(n1, n2):
   """
   -> Recebe dois parâmentros
   n1 = primeiro numero
   n2 = segundo numero
   Soma os dois e printa o resultado na tela
   Sem retorno
   Criado por Thiago Lima.
   """
   soma = n1 + n2
   print(soma)


help(soma)

#--------------------------------------------------------

#Parâmetros opcionais

def soma(n1 = 0, n2 = 0, n3 = 0):
   soma = n1 + n2
   print(soma)

soma(5,3)

#--------------------------------------------------------

# Escopo de variáveis

def teste():
   x = 1 #Variável local
   print(f'N vale: {n}, X só vale {x}, aqui dentro!')

n = 2 #Variável Global
print(f'N vale: {n}')

# Se você alterar a var global na local, é criada uma var local copia, sem alterar a global.
# para utilizar a var global sem criar a cópia, digite: global nomeVar, agora ele não cria uma nova, mas altera a global.

def funcao(b):
   global a
   a = 8
   b += 4
   c = 2
   print(f'A dentro vale: {a}')
   print(f'B dentro vale: {b}')
   print(f'C dentro vale: {c}')

a = 5
funcao(a)
print(f'A fora vale: {a}')

#--------------------------------------------------------

# Retorno de valores
# Serve para quando nós precisamos retornar resultados que não estão pré-formatados, por exemplo na soma, ao invés de já retornar a soma no print, eu posso retornar somente o resultado:

def somar(a=0, b=0, c=0):
   s = a + b + c
   return s

# 1° forma de receber:

r1 = somar(3,4,5)
r2 = somar(4,5)
print(f'Meus resultados deram {r1} e {r2}')

# 2º forma de receber

print(somar(3,4,7))

# Você pode retornar qualquer tipo de valor bool, str, int ou float

#--------------------------------------------------------

# Exercicios

# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(ano):
   from datetime import date
   atual = date.today().year
   idade = atual - ano
   if idade < 16:
      return f'Com {idade} anos o voto é NEGADO'
   elif 16 <= idade < 18 or idade > 65:
      return f'Com {idade} anos o voto é OPCIONAL' 
   else:
      return f'Com {idade} anos o voto é OBRIGATÓRIO' 

nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))

#Liberar para lista de exercicios em duplas:
