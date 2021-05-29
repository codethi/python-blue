# Getters e Setters (Obter e Definir)

# Na aula passada a gente protejeu nosso atruibuto saldo pra ele não ser modificado sem acessar os métodos sacar e depositar, além disso nós impedimos que ele seja mostrado sem ser pelo metodo extrato.
class Conta:
   def __init__(self, titular, saldo=0):
      self.titular = titular
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
      print(f'{self.titular} seu saldo é {self.__saldo:.2f}')

# Porém o método extrato é um método que retorna uma String formatada.

# E se eu quiser pegar apenas o valor do saldo? Eu não posso pegar pelo atributo direto porque ele está protegido, por isso criamos os metodos Getters:

   def get_saldo(self): # Essa nomenclatura é uma boa prática em programação.
      return self.__saldo

# Sim, para tudo que queremos que nossa classe faça, temos que criar métodos, pois são as ações da classe. Com esse método get eu consigo pegar apenas o valor do saldo, vamos ver esse teste no arquivo main.py.

# Agora além de pegar o valor eu quero poder definir um novo valor para o saldo, sem ser em um saque. Para isso eu não posso colocar diretamente no atributo. Então utilizamos o metodo set():

   def set_saldo(self, saldo): # Essa nomenclatura é uma boa prática em programação.
      self.__saldo = saldo

# Agora vamos testar esse novo método no arquivo main.py

# Essa operação não é realmente algo que poderia acontecer no meu programa, mas serve apenas para exemplificar como seria a criação desses métodos.

# Se você não precisar criar métodos getters e setters, não os crie.

 