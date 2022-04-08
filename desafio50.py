soma = 0
for c in range(0,6):
    n = int(input(f'Digite o {c+1}o número: '))
    if (n%2 == 0):
        soma += n
print('A soma dos números pares é ', soma)
