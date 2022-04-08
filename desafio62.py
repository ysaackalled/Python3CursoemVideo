n = int(input('Qual é o 1o termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
c = int(input('Gostaria de ver quantos termos? ')) # TERMOS DA P.A

while c >= 1:
    if c == 10:
        print(f'{n}, ', end='')
    elif c == 1:
        print(f'{n}', end='...\n')
        c = int(input('Gostaria de ver mais quantos termos? '))
        if c == 0:
            print('FIM!')
    else:
        print(f'{n}, ', end='')
    c -= 1
    n += r

