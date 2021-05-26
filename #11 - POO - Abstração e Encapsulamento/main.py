# A abstração é o ponto de partida para a criação de programas utilizando POO. Trata-se da capacidade de extrair dos personagens ou dos itens presentes no contexto, suas principais características, criando, dessa forma, objetos.

from conta import Conta

if __name__ == '__main__': # Garante que esse código será executado apenas nesse arquivo.
   nome = str(input('Digite o nome do titular: '))
   saldo = float(input('Digite o saldo da conta: '))
   conta001 = Conta(nome, saldo)

   while True:

      opcao = int(input(''' 
         Escolha sua opção:
         [ 1 ] Sacar
         [ 2 ] Depositar
         [ 3 ] Ver extrato
         [ 4 ] Sair

      '''))
      if opcao == 1:
         while True:
            saque = float(input('Quanto você quer sacar? R$ '))
            conta001.sacar(saque)
            resp = str(input('Quer continuar sacando? [S/N]: ').strip().upper()[0])
            if resp in 'N':
               break
      elif opcao == 2:
         while True:
            deposito = float(input('Quanto você quer depositar? R$ '))
            conta001.depositar(deposito)
            resp = str(input('Quer continuar depositando? [S/N]: ').strip().upper()[0])
            if resp in 'N':
               break
      elif opcao == 3:
         conta001.extrato()
      elif opcao == 4:
         print('Até a próxima!')
         break
      else:
         print('Opção incorreta, tente novamente!')


# Esse código acima e o código do arquivo conta.py estão funcionais, porém ainda não estão 100% enquadrados no conceito de OO, isso porque os meus atributos ainda estão frágeis, olha o que podemos fazer para "quebrar" nosso código:

   conta001.saldo = 8000.00 # Burlo o sistema

   conta001.extrato()

# Pra resolver isso vamos no arquivo conta.py mudar algumas coisas.

# Após colocar os underlines, o seus atributos são "protegidos", mas isso não impede que eu os chame aqui na main.py com esse código:

   conta001._Conta__saldo = 50 # Eu consigo alterar, mas o Python me avisa que não é uma boa prática.

   conta001.extrato()

# Encapsular os dados de uma aplicação significa evitar que estes sofram acessos indevidos. 
# Torna-lo 'privados' e construir métodos para avitar alteralções externas(como no exemplo do extrato), é utilizar o conceito de encapsulamento da OO.


# Vamos exercitar abstração e encapsulamento:

# Faça um programa que simule um televisor criando-o como um objeto. ​
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.​
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.​