from random import randint
vitorias = 0

while True:
    c = randint(0, 1)
    n = str(input('Par ou Impar(P/I)? ').upper())
    print(n)
    if n == 'P' and c == 0:
        vitorias += 1
        print('Ganhou!')
    elif n == 'I' and c == 1:
        vitorias += 1
        print('Ganhou!')
    else:
        break
print(f'Errou! Ganhou {vitorias} vezes.')
    