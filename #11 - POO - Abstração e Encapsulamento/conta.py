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

# Nesse arquivo para encapsular(proteger) minha classe eu preciso colocar 2 underlines antes do nome de todos os atributos. Isso deixa eles "privados".
# Além disso eu criei o metodo extrato() que também encapsula informações em minha classe.
