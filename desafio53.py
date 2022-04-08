frase = str(input('Digite uma frase: '))
frase = frase.strip().lower().split()
frase = ''.join(frase)
esarf = ''
tamanho = len(frase)

for c in range(tamanho -1 , -1, -1):
    esarf += frase[c]

print (f'Sua frase de trás pra frente fica: \n\033[31m{esarf}\033[m')

if (esarf == frase):
    print('Sua frase é um \033[31mpalindromo\033[m!')
else:
    print('Não é um \033[31mpalíndromo\033[m.')
