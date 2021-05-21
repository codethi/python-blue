# Vamos relembrar um pouco do laço FOR

# Contagem regressiva para o ano novo com FOR

from time import sleep

for cont in range(10, 0, -1):
   print(cont)
   sleep(1)
print('FELIZ ANO NOVOOO!')

# Agora com o While

cont = 10

while cont != 0:
   print(cont)
   sleep(1)
   cont -= 1 # Diminui 1 do cont a cada volta do laço
print('FELIZ ANO NOVOOO!')

# Mas então pra que existe o while?
# Ele existe para quando nós não sabemos o limite de 'voltas' que nosso laço vai dar, por exemplo:

# Nós escrevemos esse código com o For:

for c in range(1, 4):
   n = int(input('Digite um valor: '))
print('Fim')

# Mas e se eu não saber quantos valores ele tem que digitar? Dai eu posso escrever assim:

n = 1
while n != 0: # O while é um laço com condição de parada, ENQUANTO o n for diferente de zero, faça...
   n = int(input('Digite um valor: '))
print('Fim')

# Outro exemplo

n = 1
r = 'S'
while r == 'S': 
   n = int(input('Digite um valor: '))
   r = input('Quer continuar? [S/N] ').upper()
print('Fim')

# Com o while eu posso criar laços até indeterminadas vezes, eu não preciso ter um limite.

# IMPORTANTE:

# Se você sabe a quantidade de vezes que você precisa fazer o laço, ou seja, se vc tem um valor final de voltas, você pode utilizar o FOR ou o WHILE, mas o FOR é o mais indicado.

# Agora se você NÃO sabe quantas vezes esse laço vai ser feito, você só pode utilizar o WHILE.

# Exemplo lúdico:
# Imagine que seu chefe peça pra você anotar a idade de todo mundo que chegar no seu balcão, até as 18h.

# Você sabe quantas pessoas vão ir no seu balcão?
# Não, você só sabe que você tem que marcar a idade delas e que tem que ser até as 18h.
# Então você precisa usar o while =D

# Vamos fazer mais um exemplo:

n = 1 # isso é gambiarra, while com break
par = impar = 0
while n != 0:
   n = int(input('Digite um valor: '))
   if n != 0:
      if n % 2 == 0:
         par += 1
      else:
         impar += 1

print(f'Você digitou {par} numeros pares e {impar} números impares!')

#EXERCÍCIOS

#---------------------------------------------------------------------------


# Intemrrompendo laços while

# As linguagens de programação tem normalmente três estruturas de repetição: FOR, WHILE e o Repet ou Do While

#Mas o Python só tem o For e o While, porém podemos simular o DO WHILE com o que vamos ver agora:

# Em python podemos criar um laço infinito e determinar uma condição no "final" dele, vamos exemplificar isso:

# Com o while normal:

n = s = 0

while n != 999:
   n = int(input('Digite um número: '))
   s += n
s -= 999
print(f'A soma vale {s}')

# Com o while infinito:

n = s = 0

while True:
   n = int(input('Digite um número: '))
   if n == 999:
      break
   s += n
print(f'A soma vale {s}')

# Jogo de Par ou impar
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint # biblioteca para gerar números inteiros aleatorios

# Variável para contar as vitórias
vitoria = 0
# Laço infinito até o break 
while True:
   # Pega o numero do usuario 
   jogador = int(input('Diga um valor: ')) 
   # Gera um valor aleatório de 0 a 10
   computador = randint(0, 10) 
   # Soma o valor do user com do pc
   total = jogador + computador 
   # Inicializa a variável tipo
   tipo = ' ' 
   # Laço para repetir a pergunta de par ou impar até que seja digitado P ou I
   while tipo not in 'PI': 
      # Recebe P ou I do user, tirando os espaço, colcoando a letra em maiuscula e pagando apenas a primeira letra
      tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
   # Mostrando o resultado do jogador mais o computador
   print(f'Você jogou {jogador} e computador {computador}. Total de {total}')

   # Verificando se eu digitei P no tipo
   if tipo == 'P':
      # Verificando se o total é par
      if total % 2 == 0:
         # Mostrando que venci
         print('Você venceu!')
         # Somando mais UMA vitória para mim
         vitoria += 1
      else:
         # Senão eu perdi
         print('Você perdeu!')
         # Dai o laço infinito para
         break
   # Veirificando de digitei I
   elif tipo == 'I':
      # Verificando se o total foi impar
      if total % 2 != 0:
         # Mostra que venci
         print('Você venceu!')
         # Adiciona mais UMA vitória pra mim
         vitoria += 1
      else:
         # Mostra se perdi
         print('Você perdeu!')
         # Para o laço infinito
         break
   # Se venci, fala para eu continuar o jogo e volta pro começo do laço infinito
   print('\nVamos jogar novamente...')
# Se entrar no break finaliza o jogo e mostra minhas vitórias.
print(f'GAME OVER! Você venceu {vitoria} vezes')

#------------------------------------------------

# Exercicio