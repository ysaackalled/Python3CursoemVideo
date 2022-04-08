km = int(input('Qual a distancia da viagem? '))

if (km <= 200):
    preco = (km*0.5)
else:
    preco = (km*0.45)
    
print('O valor para sua viagem de {}km é de R${:.2f}'.format(km, preco))
