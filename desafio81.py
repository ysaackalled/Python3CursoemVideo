lista = []
while True:
    lista.append(int(input('Digite: ')))
    if 999 in lista:
        lista.remove(999)
        print('Fim.')
        break

lista.sort(reverse=True)
print()
print(f'Foram digitados {len(lista)} números.')
print(f'A lista decrescente: {lista}')

if 5 in lista:
    print(f'O num 5 foi encontrado no indice {lista.index(5)}')
else:
    print('Não existe 5 na lista.')

