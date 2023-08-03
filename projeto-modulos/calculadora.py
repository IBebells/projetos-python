

def mult (n1, n2):
   return n1 * n2 

def soma (n1, n2):
   return n1 + n2

def div (n1, n2):
   if n2 == 0:
      print("Não existe divisão por zero!")
   else:
      return n1/n2

def subt (n1, n2):
   return n1-n2

def pot(n1, n2):
   return n1 ** n2

def converte_binario (numero):
   opcao = int(input("Você quer converter um número para [1]Decimal ou [2]Binário: "))
   if opcao == 1:
      return bin(numero)[2:]
   elif opcao == 2:
      return int(numero, 2)

def raiz (radicando, indice):
   return radicando ** (1/indice)   

