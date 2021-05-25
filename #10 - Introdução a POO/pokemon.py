# Todo molde é criado dessa forma:

# class é uma palavra reservada para meu molde, já o Pokemon é um nome qualquer que eu estou dando para minha classe, usamos a convenção camel-case, onde todas as palavras são escritas com a primeira letra maiuscula e tudo junto.
class Pokemon:
   # Para criar(construir) os atributos dentro de uma class em Python, nós precisamos utilizar essa função:

   def __init__(self, nome, tipo, ataque, defesa): # Função para construir meus atributos no objeto(Função construtora).
      #pass # Com essa palavra reservada o Python deixa passar a necessidade de código nessa classe.
      print(f'Construindo objeto...{self}')
      # Esse self é a variável de referencia que vai criar um novo objeto Pokemon na memória, para eu saber qual objeto está sendo criado, uma vez que eu posso criar vários objetos a partir dessa classe(molde).
      
      # self é a referencia, nome é um atributo, o nome depois do igual é o atributo recebido no construtor.
      self.nome = nome 
      self.tipo = tipo
      self.ataque = ataque
      self.defesa = defesa

   # Métodos(ações) dessa classe

   def estadoFinal(self): # Recebe self para indicar de qual objeto eu estou referenciando minha função.
      print(f'A pontuação do {self.nome} de ataques é: {self.ataque} e de defesa é: {self.defesa}')

   def atacar(self, valorAtaque):
      self.ataque -= valorAtaque

   def defender(self, valorDefesa):
      self.defesa -= valorDefesa

   