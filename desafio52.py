primo = int(input('Digite o número: '))
total = 0

for c in range (1, primo+1):
    if (primo%c == 0):
        total +=1
        print(f'\033[31m{c}\033[m', end =' ')
    else:
        print(f'{c}', end =' ')
print('')
if total == 2:
    print('Primo.')
else:
    print(f'Não primo, esse número tem {total} divisores.')
