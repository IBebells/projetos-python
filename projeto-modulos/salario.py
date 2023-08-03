#inserir salario
#calcular bonus
#calcular desconto 
import calculadora as cal

def recebe_dados():
    return float(input("Digite o seu salário: "))

def salario_bonus(bonus):
    salario = recebe_dados()
    print("Seu sálario com bonus é:{res:.2f}".format(res = cal.soma(salario, bonus)))

def salario_desconto(desconto):
    salario = recebe_dados()
    print("Seu sálario com desconto é:{res:.2f}".format(res = cal.subt(salario, desconto)))   

def converte_salario():
    salario = recebe_dados()
    lista_moedas = ['Dólar Americano', 'Euro', 'Iene Japonês', 'Dólar Canadense', 'Peso Argentino']
    for index, moedas in enumerate(lista_moedas ):
        print(f"[{index+1}] - [{moedas}]")
    moeda = int(input(f"Conforme a lista acima para qual moeda você quer converter seu salario: "))

    if moeda == 1:
        print(f"Seu sálario em dolares é US${cal.mult(salario, 0.21):.2f}")
    elif moeda == 2:
        print(f"Seu sálario em euros é €{cal.mult(salario, 0.18):.2f}")
    elif moeda == 3:
        print(f"Seu sálario em ienes japones é ¥{cal.mult(salario, 28.76):.2f}")
    elif moeda == 4:
        print(f"Seu sálario em dolares canadenses é C${cal.mult(salario, 0.27):.2f}")
    elif moeda == 5:
        print(f"Seu sálario em pesos argentinos é ${cal.mult(salario, 55.13):.2f}")
    else:
        print("Valor inserido inválido!")
        converte_salario()

converte_salario()
