n = int(input('Tabuada Fatorial\nDigite o número: '))
fat = 1
while n > 1:
    print(f'{n} x ', end ='')
    fat *= n
    n -= 1
    if n == 1:
        print('1 ', end = '')
print(f'= {fat}')
