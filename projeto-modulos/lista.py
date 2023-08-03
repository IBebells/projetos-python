#recebe uma lista na sequencia de fibonacci feita pela função fibo()
#retorna a lista apenas com os numeros impares

import fibonacci as fib
import calculadora as cal

def lista_impares (lista):
    for index, numero in enumerate(lista):
        if numero %2 == 0:
            del lista[index]
    return lista

#recebe uma lista e ordena em ordem crescente ou descrescente
def ordena_lista(lista):
    ordem = int(input("Escolha como você quer ordenar [1]Crescente ou [2]Decrescente: "))
    if ordem == 1:
        lista.sort()
    elif ordem == 2:
        lista.sort(reverse = True)
    else:
        print("Valor inserido inválido")
        ordena_lista(lista)
    return lista

#recebe uma lista de numeros e retorna todos somados
def soma_lista(lista):
    soma_total = 0 #varivel que conterá a soma de todos os números
    for numero in lista:
        soma_total = soma_total + numero
    return soma_total


def maior_menor(lista):
    maior_numero = max(lista)
    menor_numero = min(lista)
    print(f"O maior número é {maior_numero}\nO menor número é {menor_numero}")

lista = [50,105,19]

maior_menor(lista)