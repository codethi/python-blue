from conta import Conta

if __name__ == '__main__': # Garante que esse código será executado apenas nesse arquivo.
   conta001 = Conta('Thiago', 500.00)

   while True:

      opcao = int(input(''' 
         Escolha sua opção:
         [ 1 ] Sacar
         [ 2 ] Depositar
         [ 3 ] Ver extrato
         [ 4 ] Ver saldo
         [ 5 ] Mudar Saldo
         [ 6 ] Sair

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
         saldoConta = conta001.get_saldo() # Utilização do método get.
         print(saldoConta)    
      elif opcao == 5:
         conta001.set_saldo(300)     
      elif opcao == 6:
         print('Até a próxima!')
         break
      else:
         print('Opção incorreta, tente novamente!')


