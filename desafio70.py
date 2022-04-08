minpreco = 0
minproduto = ''
total = 0
lista_caro = []
while True:
    produto = str(input('Qual produto? '))
    preco = int(input('Qual o preço? '))
    total += preco
    if minpreco == 0:
        minpreco = preco
    if preco < minpreco:
        minpreco = preco
        minproduto = produto
    if preco > 1000:
        lista_caro.append(produto)
    cont = input('Deseja continuar(S/N)?' ).upper()
    if cont != 'S':
        break

print(f'Total gasto na compra: R${total:.2f}')
print(f'Quantos produtos custam mais de R$1000.00 : {lista_caro}')
print(f'Produto mais barato: {minproduto}, custou R${minpreco:.2f}')