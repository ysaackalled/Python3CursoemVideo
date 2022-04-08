from random import randint

tupla = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
menor = 100
maior = 0

for c in tupla:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    print(f'{c} ', end='')
    
print()
print(f'O menor número sorteado foi: {menor}.')
print(f'O maior número sorteado foi: {maior}.')
