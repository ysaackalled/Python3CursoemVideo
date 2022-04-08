tupla = ('Arroz', 21.99, 'Feijão', 8.49, 'Picanha', 98.99, 'Coca Cola', 8.49, 'Suco de Laranja', 9.49,'Sardinha', 6.49)

for index, c in enumerate(tupla):
    if index % 2 == 0:
        print(f'{c}', end ='')
        print('_'*(40-(len(tupla[index]))), end='')
    else:
        print(f'R${c:.2f}')
