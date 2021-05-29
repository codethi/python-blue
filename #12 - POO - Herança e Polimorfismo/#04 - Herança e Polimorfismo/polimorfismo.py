# Para criar nossa playlist, que irá armazenar nossos programas, nós vamos vamos utilizar o conceito de polimorfismo, que é a capacidade que a superclasse tem de executar uma ação diferente em casa subclasse herdeira.

# Por exemplo:

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

class Filme(Programa): 
   def __init__ (self, nome, ano, duracao):
      super().__init__(nome, ano)
      self.duracao = duracao
   
   def imprime(self):
      print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes}')

class Serie(Programa):
   def __init__ (self, nome, ano, temporadas):
      super().__init__(nome, ano)
      self.temporadas = temporadas
   
   def imprime(self):
      print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}')

# Eu quero colocar todos os objetos instanciados dentro de uma playlist e mostra-la para o usuário. Pra isso eu posso coloca-las em uma lista:

vingadores = Filme('guerra infinita', 2018, 160)
vingadores.dar_like()

friends = Serie('friends', 1994, 10)
friends.dar_like()
friends.dar_like()

filmes_e_series = [vingadores, friends]

for programa in filmes_e_series:
   print(f'{programa.nome} - {programa.duracao} - {programa.likes}')

# Vamos resolver esse problema acima com o código abaixo, verificando se o objeto tem duracao ou temporada.

for programa in filmes_e_series:
   if hasattr(programa, 'duracao'):
      detalhes = programa.duracao
   else:
      detalhes = programa.temporadas
   print(f'{programa.nome} - {detalhes} - {programa.likes}')

# Mas esse código ainda não está bom, por que se eu tiver outras subclasses com suas especifidades, esse código ficaria gigante.

# Por isso é importante dizer que as classes precisar ser responsáveis pelo que ela precisa fazer, se isso acontecer quer dizer que as classes são coesas.

# Por isso iremos colocar o imprimir nas respectivas classes e não no programa principal, pois elas possuem especificidades diferentes. Então vamos criar o método imprime nas duas classes, e nosso for ficará assim:

for programa in filmes_e_series:
   programa.imprime()

# Mas ainda da pra melhorar mais essa forma de imprimir, existem métodos especiais em Python, que sempre estão entre 2 underlines, como o __init__.

# Para imprimir dados da minha classe sem usar esse método imprimir, nós tempo o método especial __str__ que retorna uma representação textual da minha classe, vamos alterar nosso programa:


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

class Filme(Programa): 
   def __init__ (self, nome, ano, duracao):
      super().__init__(nome, ano)
      self.duracao = duracao
   
   def __str__(self):
      return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes}'

class Serie(Programa):
   def __init__ (self, nome, ano, temporadas):
      super().__init__(nome, ano)
      self.temporadas = temporadas
   
   def __str__(self):
      return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}'



vingadores = Filme('guerra infinita', 2018, 160)
vingadores.dar_like()

friends = Serie('friends', 1994, 10)
friends.dar_like()
friends.dar_like()

filmes_e_series = [vingadores, friends]

for programa in filmes_e_series:
   print(programa)