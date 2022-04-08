salario = float(input('Qual é o seu salário? '))
aumento = int(input('Qual é o aumento (em porcentagem? '))
salau = salario + (salario * aumento/100)
print('O salário final com {}% de desconto é {}'.format(aumento, salau))