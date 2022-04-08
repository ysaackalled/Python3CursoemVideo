lista = []
for c in range(0, 10):
    print(c)
    n = int(input('Número: '))
    if n in lista:
        print('Esse número não pode ser adicionado!')
    else:
        lista.append(n)
        
print(sorted(lista))
