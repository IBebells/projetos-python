#recebe um numero que indica o range da sequencia de fibonacci
def fibo(numero):
    lista_fibo = [0,1]
    
    while (len(lista_fibo) - 1) != numero: 
        ultimo_numero = lista_fibo[-1]
        penultimo_numero = lista_fibo[-2]
        proximo_numero = ultimo_numero + penultimo_numero

        lista_fibo.append(proximo_numero)
    
    del lista_fibo[0]
    
    return lista_fibo
