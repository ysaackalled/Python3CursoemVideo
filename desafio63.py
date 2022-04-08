print('Sequencia de Fibonacci!')
n = int(input('Quantos elementos quer ver? '))
n1 = 0
n2 = 1
soma = n1+n2
print(n1, n2, end=' ')
while n >= 3:
    soma = n1 + n2
    print(soma, end=' ') 
    n1 = n2
    n2 = soma       
    n -= 1

