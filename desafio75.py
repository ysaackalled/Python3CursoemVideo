tupla = (int(input('1o num: ')), int(input('2o num: ')), int(input('3o num: ')), int(input('4o num: ')))
print(tupla)
tres = 0

print(f'O número 9 apareceu {tupla.count(9)} vezes.')

for index, c in enumerate(tupla):
    if c == 3 and tres == 0:
        print(f'O número três aparece a primeira vez na {index+1}ª posição')
        tres += 1

print('Números pares: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end ='')
