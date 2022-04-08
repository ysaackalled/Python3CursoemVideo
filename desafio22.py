nome = input('Qual é seu nome completo? ')

print('capitalizado: {}'.format(nome.upper()))
print('minusculo: {}'.format(nome.lower()))
nomeLetras = (nome.split())
primeiro = len(nomeLetras[0])
nomeLetras = ''.join(nomeLetras)
print('Seu nome tem {} letras.'.format(len(nomeLetras)))
print('Seu primeiro nome tem {} letras.'.format(primeiro))
