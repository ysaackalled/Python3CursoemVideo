sx = str(input('Qual o seu sexo: '))

while (sx != 'f') and (sx != 'm'):
    sx = sx.lower()
    print('ERRO!')
    sx = str(input('Qual o seu sexo: '))
    