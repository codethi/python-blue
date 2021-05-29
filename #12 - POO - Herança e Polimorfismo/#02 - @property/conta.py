# Property

# Vamos imagina que queremos criar uma regra para o nosso atributo titular, onde todo nome escrito terá que ter a primeira letra maiúscula. A gente pode fazer isso direto na main(), porém lembre sempre, que toda ação que a gente deseja fazer com a classe, devemos fazer a partir de métodos!
class Conta:
   def __init__(self, titular, saldo=0):
      self.__titular = titular # Atributo privado para o @property funcionar
      self.__saldo = saldo

   def sacar(self, valor):
      if valor != 0:
         if self.__saldo < valor:
            print(f'Você não tem R$ {valor:.2f} para sacar')
            self.extrato() 
         else:
            self.__saldo -= valor
            print(f'Você sacou: R$ {valor:.2f}')
            self.extrato()       
      else:
         print('Você não pode sacar 0 reais')
         
   def depositar(self, valor):
      self.__saldo += valor
      print(f'Você depositou: R$ {valor:.2f}')
      self.extrato()   

   def extrato(self):
      print(f'{self.__titular} seu saldo é {self.__saldo:.2f}')

   def get_saldo(self): 
      return self.__saldo

   def set_saldo(self, saldo): 
      self.__saldo = saldo

# Vamor criar então o método get_titular para retornar o nome do titular com a letra maiuscula sempre!

   def get_titular(self):
      return self.titular.title() 

# Vamos testar no arquivo main.py

# Isso funciona normalmente, porém eu não quero que no arquivo main.py eu chame o método get, eu quero mostrar o titular apenas com conta001.titular, porém a gente já viu que isso não é muito seguro e assim eu não consigo tratar o retorno, colocando como maiusculo.

# Então eu quero que o conta001.nome, funcione, chamando um metodo e retornando essa minha alteração.

# Para isso usamos o @property:

   @property # Isso fala que o método representa uma propriedade(atributo)
   def titular(self):
      return self.__titular.title()

# Mas pra isso funciona de forma efetiva, nosso atributo precisa ser protegido. 

# Isso funciona também para o set:

   @titular.setter # Siginifica que para esse atributo titular o metodo será setter(definir)
   def titular(self, titular):
      self.__titular = titular

   