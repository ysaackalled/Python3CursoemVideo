r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if((r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2)):
    print('As retas \033[0;31m{}\033[m, \033[0;32m{}\033[m e \033[0;34m{}\033[m \033[1mpodem\033[m formar um triangulo.'.format(r1, r2, r3))
else:
    print('As retas \033[0;31m{}\033[m, \033[0;32m{}\033[m e \033[0;34m{}\033[m \033[1mnão podem\033[m formar um triangulo.'.format(r1, r2, r3))

