vel = int(input('Qual a velocidade do carro? '))
print('Você passou a {} Km/h.'.format(vel))

if(vel > 80):
    print('Você excedeu o limite. Deve pagar uma multa de R${}.00'.format((vel-80)*7))
else:
    print('Tudo certo!')
