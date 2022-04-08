n = int(input('Qual é o 1o termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
c = 10 # TERMOS DA P.A
while c >= 1:
    if c == 10:
        print(f'{n}, ', end='')
    elif c == 1:
        print(f'{n}', end='...')
    else:
        print(f'{n}, ', end='')
    c -= 1
    n += r
