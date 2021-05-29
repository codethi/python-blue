# Herança no mundo real é o que recebemos dos nosso tutores, parentes ou pais, pode ser dinheir, imóveis, dividas, caracteristicas ou ações em comum.

# Em OO, nós podemos também fazer as classes herdarem as caracteristicas(atributos) e ações(métodos), de outra classe.

# No exemplo da nossa plataforma de streaming, vimos que filmes e series possuem atributos e métodos semelhantes, então nós podemos criar uma terceira classe Programa() 

class Programa():
   def __init__ (self, nome, ano):
      self.__nome = nome.title()
      self.ano = ano
      self.__likes = 0

   @property
   def nome(self):
      return self.__nome

   @nome.setter
   def nome(self, nome):
      self.nome = nome

   @property
   def likes(self):
      return self.__likes

   def dar_like(self):
      self.__likes += 1

class Filme(Programa): # Agora o filme herda tudo que programa tem atributos e metodos.
   def __init__ (self, nome, ano, duracao):
      self.__nome = nome.title()
      self.ano = ano
      self.duracao = duracao
      self.__likes = 0

   

class Serie(Programa):
   def __init__ (self, nome, ano, temporadas):
      self.__nome = nome.title()
      self.ano = ano
      self.temporadas = temporadas
      self.__likes = 0


vingadores = Filme('guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

friends = Serie('friends', 1994, 10)
friends.dar_like()
friends.dar_like()
print(f'Nome: {friends.nome} - Ano: {friends.ano} - Duração: {friends.temporadas} - Likes: {friends.likes}')

# Erro aconteceu porque o nome e o like estão protegidos na class mãe que é Programa(), pra resolver isso podemos mudar de 2 underlines para apenas 1, por convenção ele continua protegido, porém o nome dele não é mudado, na hora da chamada para executar os métodos.

# Nosso código ainda está repetitivo, pois temos atributos iguais nas 3 classes, vamos resolver isso agora.

# Vamos retirar os atributos repetidos e vamos chamar nossa classe mãe com a função super(), depois vamos entrar no método construtor __init__ e passar os parêmetros de nome e ano, para que minha classe mãe seja responsável de constrir esses atributos e não a classe filha.

class Filme(Programa): 
   def __init__ (self, nome, ano, duracao):
      super().__init__(nome, ano)
      self.duracao = duracao

class Serie(Programa):
   def __init__ (self, nome, ano, temporadas):
      super().__init__(nome, ano)
      self.temporadas = temporadas


# Agora vamos criar em nossa plataforma de streaming, uma playlist de filmes e séries utilizando o documento polimosrfismo.py