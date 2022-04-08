nome = input('Digite o nome completo: ')
nomelista = nome.split()
ultimo = len(nomelista)
print('O primeiro nome é {}.'.format(nomelista[0]))
print('O último nome é {}.'.format(nomelista[ultimo-1]))

