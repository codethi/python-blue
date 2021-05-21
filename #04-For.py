# Até agora a gente aprendeu a desviar das coisas, agora vmaos aprender a repetir elas!

# Imagina que nós queremos escrever na telá olá 5 vezes, nós teriamos que colcoar:

print('Olá')
print('Olá')
print('Olá')
print('Olá')
print('Olá')

# Mas e se eu quiser escrever isso 500 vezes? Seria inviável, por isso temos o laço for, podemos substituir o código de cima por:

for c in range(1, 6): # De 1 a 6 porque o range ignora o ultimo número.
   print('Olá')
print('Fim')

# O laço for é chamado de laço com variável de controle, caso acima, o c é a variável de controle.

# Outro exemplo, pra entendermos variáveis de controle:

for c in range(0, 5):
   print(c) # Vai mostrar uma contagem crescente

# Para contagens descrescentes utilize:

for c in range(5, 0, -1): # começa no 5, tira 1 (-1), até o 1 (pois o útimo é ignorado)
   print(c)

# Para pular de dois em dois:

for c in range(0, 7, 2): # começa no 0, pula de 2 em 2, até o 6 (pois o útimo é ignorado)
   print(c)

# Vamos a mais um exemplo:

n = int(input('Digite um número: '))

for c in range(0, n+1): # Li o n e utilizei dentro do range para contagem.
   print(c)
print('Fim')

# Agora vamos receber o incio do range, o fim e o passo:

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))


for c in range(i, f+1, p): 
   print(c)
print('Fim')

# Vamos pedir varios valores no for, através do input e somar todos eles:

s = 0
for c in range(0, 4):
   n = int(input('Digite um número: '))
   s += n
print(f'A soma de todos os numeros é {s}')

# O in pode ser usado para Strings

for letra in 'Thiago Veiga Lima':
   if letra == 'e':
      print(f'Achei a letra {letra}')
print('Fim')


# EXERCÍCIOS

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for cont in range(10, -1, -1):
   print(cont)
   sleep(1)
print('FELIZ ANO NOVOOO!')




