casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do seu salário? '))
anos = int(input('Quer pagar em quantos anos? '))
mensalidades = anos * 12
val_mensal = casa / mensalidades
val_limite = (sal * 30/100)



if (val_mensal > (val_limite)):    
    print(f'Emprestimo negado! O valor da prestação de R${val_mensal:.2f} excede 30% do salário(R${val_limite:.2f})')
else:
    print(f'Emprestimo concedido! O valor da prestação de R${val_mensal:.2f} não excede 30% do salário(R${val_limite:.2f})')
