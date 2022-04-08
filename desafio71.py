print('Cédulas disponíveis: R$50, R$20, R$10, R$1 ')
while True:
    nvalor = int(input('Quanto deseja sacar? (>0)'))   
    if nvalor <= 0: 
        break 
    notas50 = nvalor//50
    nvalor = (nvalor - (50*notas50))
    notas20 = nvalor//20
    nvalor = (nvalor - (20*notas20))
    notas10 = nvalor//10
    nvalor = (nvalor - (10*notas10))
    notas1 = nvalor//1
    nvalor = (nvalor - (notas1))
    print(f'Notas de 50: {notas50}')
    print(f'Notas de 20: {notas20}')
    print(f'Notas de 10: {notas10}')
    print(f'Notas de 1: {notas1}')

