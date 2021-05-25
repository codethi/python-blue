# Vamos ao conceito de POO:

# A programação orientada a objetos é um modelo de programação onde diversas classes possuem características que definem um objeto na vida real. Cada classe determina o comportamento do objeto definido por métodos e seus estados possíveis definidos por atributos.

# No nosso exemplo da Pokedex um objeto seria um pokemon, porém antes de criar esse objeto eu preciso de um molde, que irá receber os atributos(caracteristicas) e os métodos(ações), em comum que todo objeto pokemon terá:

# Para já utilizar as boas práticas de POO, vamos criar um novo arquivo que iremos chamar de pokemon, esse arquivo será nosso molde de pokemons.

from pokemon import Pokemon # Importa do arquivo pokemon a classe Pokemon.

# print(Pokemon()) # Vai mostrar o local na memoria que Python irá criar para essa classe

# Vamos criar(instanciar) um objeto a partir da classe Pokemon

# pokemon = Pokemon() # pokemon é uma variável de referencia a classe Pokemon

# print(pokemon)

# Agora, vamos criar os atributos e métodos da nossa classe no arquivo pokemon.py

# Vamos criar um pokemon novo atribuindo os atributos requeridos:

pokemon1 = Pokemon('Pikachu', 'Elétrico', 52, 43)
pokemon2 = Pokemon('Charmander', 'Fogo', 55, 40)

# Já criamos os dois objetos de pokemon, com atributos em comum, agora vamos mostrar esse valores dos atributos na tela:

print(pokemon1.nome) # O ponto serve para entrar no objeto e buscar um atributo e nesse caso, mostrar o valor que foi guardado dentro de nome.

# Vamos praticar essa criação de atributos!

   # Crie uma classe chamada Pokemon em um arquivo chamado pokemon.py
   # Crie a função construtora dos atributos
   # Receba a referência do próprio objeto na função
   # Receba também como argumentos essas propriedades: nome, tipo, ataque e defesa
   # Através da referencia defina os atributos da classe, recebendo as propriedades do construtor.
   # Crie um arquivo chamado main.py
   # Nesse arquivo(main.py) instancie dois objetos pokemon, passando os atributos de cada um.
   #Mostre na tela:
      # O nome do segundo objeto
      # O tipo do primeiro objeto
      # O ataque dos dois objetos
      # A defesa do segundo objeto


#--------------------------------------------------------------------------------

# Agora vamos para o arquivo pokemon.py, para criar os métodos(ações) desse objeto.

# Vamos chamar essa função estadoFinal aqui:

# estadoFinal() # Isso vai dar um erro, por que eu preciso dizer para o Python, qual é o objeto que tem esse método.

pokemon1.estadoFinal() # Chamo o objeto pokemon1 e dentro dele, vá(ponto) para o método estadoFinal()

pokemon2.estadoFinal()

# Vamos voltar ao arquivo pokemon.py para criar os demais métodos do pokemon.

# Agora vamos executar os métodos.

pokemon1.atacar(20) # Vamos passar apenas o valorAtaque porque o self do método atacar é o objeto pokemon1 nesse caso.
pokemon1.defender(10)

pokemon2.atacar(30)

pokemon1.estadoFinal()
pokemon2.estadoFinal()

# Vamos melhorar esses métodos de ataque e defesa!

# Na classe Pokemon crie os métodos estadoFinal, atacar e defender:
   # estadoFinal recebe apenas o objeto de referencia
      # Mostre o nome do pokemon, o valor de ataque e o valor de defesa
   # atacar recebe o objeto de referencia e o valorAtaque
      # Subtraia do atributo ataque o valorAtaque
      # Só deixe ele atacar se o valor do atributo ataque for maior que ZERO
      # Quando o valor de ataque acabar mostre a mensagem que ele não pode mais atacar.
   # defender recebe o objeto de referencia e o valorDefesa
      # Subtraia do atributo defesa o valorDefesa
      # Só deixe ele defender se o valor do atributo defesa for maior que ZERO
      # Quando o valor de defesa acabar mostre a mensagem que ele não pode mais defender.


