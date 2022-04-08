import random
n1 = input('1o aluno: ')
n2 = input('2o aluno: ')
n3 = input('3o aluno: ')
n4 = input('4o aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)