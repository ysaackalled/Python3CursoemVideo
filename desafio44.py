valor = float(input('Qual o valor do produto? R$'))
print('''[ 0 ] À VISTA (Dinheiro/cheque) - 10% desconto
[ 1 ] À VISTA (Cartão) - 5% desconto
[ 2 ] 2x Cartão
[ 3+] Cartão (20% juros)''')
cond = int(input('Forma de pagamento? '))

if cond == 0:
    print(f'O produto no valor de R${valor:.2f} sai por R${(valor - (valor*10/100)):.2f} com 10% de desconto.')
elif cond == 1:
    print(f'O produto no valor de R${valor:.2f} sai por R${(valor - (valor*5/100)):.2f} com 5% de desconto')
elif cond == 2:
    print(f'O produto no valor de R${valor:.2f} sai por 2 parcelas de R${(valor/2):.2f}.')
elif cond >=3:
    print(f'O produto no valor de R${valor:.2f} sai por R${(valor + (valor * 20/100)):.2f}, dividido em {cond} parcelas de {valor/cond:.2f}.')
else:
    print('Condição inválida.')
