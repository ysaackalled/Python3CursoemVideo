n = []
for c in range(0,5):
    n.append(int(input('Digite um número: ')))
    if c == 0: 
        maior = n[c]
        menor = n[c]
        indmai = c
        indmen = c
    else:
        if n[c] > maior:
            maior = n[c]
            indmai = c
        elif n[c] < menor:
            menor = n[c]
            indmen = c

for c in n:
    print(c, end=' ')

print()
print(f'O maior número da lista é {maior}, na posição {indmai}.')
print(f'O menor número da lista é {menor}, na posição {indmen}.')
