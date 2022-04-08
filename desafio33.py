n1 = float(input('Digite o 1o numero: '))
n2 = float(input('Digite o 2o numero: '))
n3 = float(input('Digite o 3o numero: '))

menor = n1
maior = n1

if (n2 > n1) and (n2 > n3):
    maior = n2

if (n3 > n1) and (n3 > n2):
    maior = n3

if (n3 < n2) and (n3 < n1):
    menor = n3

if (n2 < n3) and (n2 < n1):
    menor = n2

print('O maior número entre {:.0f}, {:.0f} e {:.0f} é {:.0f}.'.format(n1, n2, n3, maior))
print('O menor número é {:.0f}.'.format(menor))
