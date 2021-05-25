# Hoje vamos mudar nossa forma de pensar em programação. 

# Até agora nós utilizamos a programação procedural, onde nosso código funciona através de procedimentos, execultando nosso código linha a linha, na ordem em que foi digitado.

# Mas esse tipo(paradigma) de programação já não é mais usado, pois existe alguns problemas nessa utilização que foram resolvidos com a programação orientada a objetos.

# Antes de mostrar muita teoria vamos ver o porque utilziar POO e quais vantagens teremos, para ver isso vamos mapear nosso caminho até aqui.

# Vamos imaginar que queremos criar uma Pokédex, para quem não sabe é aquela "agenda" digital que todo mestre Pokemon usa para "catalogar" todas as especies de pokemon existentes no mundo.

# Para criar essa pokedex, vamos colocar apenas algumas caracteristicas dos pokemons para não demorarmos muito.

# Cada pokemon terá:
   #nome
   #tipo
   #ataque
   #defesa

# Vamos criar dois pokemons utilizando o básico de variáveis:

nome = 'Charmander'
tipo = 'fogo'
ataque = 52
defesa = 43

nome2 = 'Pikachu'
tipo2 = 'eletrico'
ataque2 = 55
desfesa2 = 40

# Já percebeu que se quisermos criar os 890 pokemons existentes teriamos um problema de repetição de código e inconsitencia de dados bem grave.

# Quando prosseguimos com o Python vimos que podemos utilizar um dicionário para agrupar dados, com um indice amigável e de fácil utilização, para criar esses dois pokemons em dicionários podemos fazer assim:

pokemon1 = {'nome': 'Chamander', 'tipo': 'Fogo', 'ataque': 52, 'defesa': 43}
pokemon2 = {'nome': 'Pikachu', 'tipo': 'Elétrico', 'ataque': 55, 'defesa': 40}

# Percebam que meu agrupamento de dados já melhorou por que consegui manter as 'variáveis' e mudar apenas o nome do dicionário. A gente lembra também que se eu colocar isso dentro de um laço de repetição a gente pode criar uma lsita de dicionários e criar tranquilamente nossa pokedex solicitando os dados para o usuário e guardando em uma lista. Porém essa ainda não é a melhor solução.

# A gente já viu também que para organizar nosso código e realizar tarefas repetitivas nós podemos criar uma função, vamos fazer isso para esse cadastro de pokemons:

def pokedex(nome, tipo, ataque, defesa):
   pokemon = {'nome': nome, 'tipo': tipo, 'ataque': ataque, 'defesa': defesa}
   return pokemon

pokemon = pokedex('Pikachu', 'Elétrico', 55, 40)

print(pokemon['nome'])

# Ficou mais elegante, porém ainda não está bom, a minha dúvida é:
   # Se não fui eu que criei essa função, como eu vou saber qual é a chave do meu dicionário, ou como eu vou saber o que passar em cada variável ao chamar a função?
# Além disso eu quero não só cadastrar e apresentar as caracteristicas dos meus Pokemons, eu quero mostrar também as possiveis ações desse pokemon, o que ele pode fazer com os poderes dele em uma batalha, basicamente ele pode:
   # Atacar
   # Defender

# Vamos criar duas funções para esse pokemon, na função atacar, toda vez que o pokemon atacar, ele vai perder o valor de ataque, do seu ataque total, o mesmo acontecerá com a defesa:

def atacar(pokemon, valorAtaque):
   pokemon['ataque'] -= valorAtaque

def defender(pokemon, valorDefesa):
   pokemon['defesa'] -= valorDefesa

# Agora vamos criar um estado final para esse pokemon, para mostrar quais são os valores de defesa e ataque restantes para ele, após a chamada dos métodos acima.

def estadoFinal(pokemon):
   print(f'Após todos os ataques e defesas, sua pontuação final de ataques é: {pokemon["ataque"]} e de defesa é: {pokemon["defesa"]}')

# Vamos testar essas ações:

pokemon = pokedex('Pikachu', 'Elétrico', 55, 40)

atacar(pokemon, 20) # Chamo a função atacar, passo o pokemon cadastrado e o valor de ataque.
defender(pokemon, 10) # Chamo a função defender, passo o pokemon cadastrado e o valor de defesa.
estadoFinal(pokemon) # Mostro como ficou meu pokemon após o ataque e defesa.

# Para a programção procedural, esse programa está bom, funciona legal, mas e se tivessemos mais dados, ou mais funções, se isso acontecer nosso programa será frágil, com dados provavelmente inconsistentes e principalmente a execulção das funções não seriam efetivas, pois ficaria dificil de entender como elas funcionam exatamente. Além da organização se BEM dificil em grandes projetos.

# Olha um exemplo de inconsitencia de dados e má utilização das funções, eu posso por exemplo forçar um valor de ataque, sem utilizar a função:

pokemon['ataque'] -= 50
print(pokemon['ataque'])

# Com isso eu consegui burlar as regras de utilização de funções e acabei atrapalhando a correta execução do meu programa!

# Por isso iremos aprender programação orientada a objetos, esse tipo de paradigma é usado para unir os dados com as ações e tornar muito mais simples e de fácil entendimento a utilização e manutenção desse código, além de forçar a utilização das 'funções' para que ninguém burle meu sistema.

# Dados e ações em POO são chamados de:
   # Atributos
   # Métodos

# Próximos conceitos no arquivo introOO2.py


