import math
co = float(input('Digite o valor de um dos catetos: '))
ca = float(input('Digite o valor do outro cateto: '))
hip = (math.sqrt(pow(co, 2) + pow(ca, 2)))
print('O valor da hipotenusa desse triangulo é {:.2f}.'.format(hip))
