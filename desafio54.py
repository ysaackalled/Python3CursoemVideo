ant18 = 0
mais18 = 0

for c in range(0, 7):
    n = int(input('Qual é a data do seu nascimento? '))
    idade = (2022 - n)
    if (idade < 18):
        ant18 += 1
    else:
        mais18 += 1
print(f'Menores: {ant18}\nMaiores: {mais18}')