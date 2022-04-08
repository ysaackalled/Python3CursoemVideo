r1 = int(input('1a reta: '))
r2 = int(input('2a reta: '))
r3 = int(input('3a reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    if (r1 == r2) and (r2 == r3) and (r1 == r3):
        print('Equilátero.')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Isosceles.')
    else:
        print('Escaleno.')

else:
    print('Não é possivel criar esse triangulo.')