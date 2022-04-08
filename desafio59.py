opc = 0
n1 = float(input('Digite o 1o núm: '))
n2 = float(input('Digite o 2o núm: '))

while (opc != 5):  
    opc = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa   '))  
    if opc == 1:
        print(f'{n1:.0f} + {n2:.0f} = {n1+n2:.0f}')
    elif opc == 2:
        print(f'{n1:.0f} * {n2:.0f} = {n1*n2:.0f}')
    elif opc == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        elif n2 > n1:
            print(f'{n1} < {n2}')
        else:
            print(f'{n1} e {n2} são iguais.')
    elif opc == 4:
        n1 = float(input('Digite o 1o núm: '))
        n2 = float(input('Digite o 2o núm: '))
        opc = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa   '))
    else:
        print('FIM!')
    