# Métodos privados

# Vamos melhorar nosso código.

class Conta:
   def __init__(self, titular, saldo=0):
      self.__titular = titular
      self.__saldo = saldo

# Esse método sacar tem uma validação dentro dele, porém isso pode confundir outros programadores, e para melhorarmos isso vamos criar um novo método que se chama pode_sacar() para essa validação:

   def __pode_sacar(self, valor_saque): # Dois underlines tornam o médoto privado, assim como no atributo.
      return self.__saldo < valor_saque

   def sacar(self, valor):
      if valor != 0:
         if self.__pode_sacar(valor):
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

   @property
   def titular(self):
      return self.__titular.title()

   @titular.setter
   def titular(self, titular):
      self.__titular = titular

   

   