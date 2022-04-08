nasc = int(input('Nasceu em que ano? '))
idade = 2022 - nasc

if (idade < 18):
    print(f'Não está na idade de alistamento. Faltam {18 - idade} anos.')
elif(idade > 18):
    print(f'Já passou da idade de alistamento. Deveria ter se alistado a {idade - 18} anos.')
else:
    print('Está na idade para se alistar!')
