n = int(input('Digite um numero: '))
print('[ 1 ] Base Binária ')
print('[ 2 ] Base Octal ')
print('[ 3 ] Base Hexadecimal')
opc = int(input('Para qual base deseja converter? '))

if opc == 1:
    n = bin(n)
    print(n[2:])
elif opc == 2:
    n = oct(n)
    print(n[2:])
elif opc == 3:
    n = hex(n)
    print(n[2:])
else:
    print('Comando inválido!')
