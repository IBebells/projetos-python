#IMC
#recebe peso
#recebe altura
#calcula o IMC a partir dos dados

"""
    Menor que 18,5: Magreza
    Entre 18,5 e 24,9: Normal
    Entre 25,0 e 29,9: Sobrepeso
    Entre 30,0 e 39,9: Obesidade
    Maior que 40,0: Obesidade Grave
"""

import calculadora as cal

def recebe_dados():
    peso = float(input("Insira seu peso: "))
    altura = float(input("Insira sua altura: "))
    return peso, altura

def cal_imc(peso, altura):
    return cal.div(peso, cal.pot(altura,2))

def imc():
    peso, altura = recebe_dados()
    if cal_imc(peso, altura) < 18.5: status = "Magreza"
    elif cal_imc(peso, altura) >= 18.5 and cal_imc(peso, altura) < 25: status = "Normal"
    elif cal_imc(peso, altura) >= 25 and cal_imc(peso, altura) < 30: status = "Sobrepeso"
    elif cal_imc(peso, altura) >= 30 and cal_imc(peso, altura) < 40: status = "Obesidade"
    elif cal_imc(peso, altura) >= 40: status = "Obesidade Grave"

    print ("Seu IMC é: {cal_imc:.2f}\nClassificado como {status}.".format(cal_imc = cal_imc(peso, altura), status = status))
