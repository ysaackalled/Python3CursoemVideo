lista = []

for c in range(0, 5):
    n = int(input('Num: '))
    if c == 0:
        lista.append(n)
        maior = menor = n
    else:
        for index, val in enumerate(lista):
            if n > maior:
                maior = n
                lista.append(n)
            elif n < menor:
                menor = n
                lista.insert(0, n)
            elif n == val:
                lista.insert(index, n)
            elif n > val


print(lista)