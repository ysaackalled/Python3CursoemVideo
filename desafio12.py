preco = float(input('Qual é o valor do produto? '))
desc = float(input('Qual a porcentagem do desconto? '))
precof = preco - (preco * desc/100)
print ('O produto no valor de R${} sai por R${} com {}% de desconto'.format(preco, precof, desc))