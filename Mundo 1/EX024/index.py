salario = float(input('Qual o seu salario? R$'))
a1 = (((salario/100) * 10) + salario)
a2 = (((salario/100) * 15) + salario)
if salario > 1250:
    print('com seu aumento de 10% você vai receber R${:.2f}'.format(a1))
else:
    print('com seu aumento de 15% você vai receber R${:.2f}'.format(a2))