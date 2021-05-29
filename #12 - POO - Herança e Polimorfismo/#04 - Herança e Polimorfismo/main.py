# Vamos revisar os conceito vistos até aqui, abstraindo o conceito de uma plataforma streaming:

class Filme:
   def __init__ (self, nome, ano, duracao):
      self.__nome = nome.title()
      self.ano = ano
      self.duracao = duracao
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

class Serie:
   def __init__ (self, nome, ano, temporadas):
      self.__nome = nome.title()
      self.ano = ano
      self.temporadas = temporadas
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


vingadores = Filme('guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

friends = Serie('friends', 1994, 10)
friends.dar_like()
friends.dar_like()
print(f'Nome: {friends.nome} - Ano: {friends.ano} - Duração: {friends.temporadas} - Likes: {friends.likes}')

# Vimos que temos vunerabilidades em nossa classe se nosso atributo não é protegido, para isso encapsulamos os atributos que não queremos que ninguém acesse fora da nossa classe, como por exemplo nome e likes.

# Para pegar e atribuir valores aos meus atributos privados, eu posso criar métodos getters e setters. Mas nós já vimos que se fizermos isso vamos ter que trocar todas as chamadas aos meus atributos para vingadores.get_nome() por exemplo.

# Para evitar esse transtorno e deixar nosso código mais inchuto, vamos utilizar os decorators @property e/ou @nome.setter

#-------------------------------------------------------------------------------

# Nosso código está funcioanando, muito legal, porém ele está muito repetitivo, a gente copiou e colou muito código.

# Para resolver isso nós vamos utilizar o conceito de Herança no arquivo heranca.py!

 