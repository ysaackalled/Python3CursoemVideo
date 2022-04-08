tupla = ('banana', 'bola', 'abacaxi', 'pastel', 'hojetem', 'mariposa', 'jabuticaba')

for c in tupla: # VERIFICAR CADA TERMO DA TUPLA
    print (f'{c} = ', end='')
    for d in c: # VERIFICAR CADA LETRA
        if 'a' in d:
            print('a',end='')
        elif 'e' in d:
            print('e',end='')
        elif 'i' in d:
            print('i',end='')
        elif 'o' in d:
            print('o', end='')
        elif 'u' in d:
            print('u', end='')
    print()
