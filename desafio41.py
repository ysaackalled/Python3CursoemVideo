nasc = int(input('Ano de nascimento: '))
idade = 2022 - nasc

if (idade <= 9):
    print('Categoria: MIRIM')
elif (idade <= 14):
    print('Categoria INFANTIL')
elif (idade <= 19):
    print('Categoria: JUNIOR')
elif (idade <= 20):
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')