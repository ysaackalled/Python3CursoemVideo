altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura? '))
metragem = altura * largura
tinta = metragem / 2
print('Sua parede possui {} m² e serão necessários {} litros de tinta.'.format(metragem, tinta))