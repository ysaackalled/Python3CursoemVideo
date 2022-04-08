while True:
    n = int(input('Número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print (f'{n} x {c} = {c*n}')
