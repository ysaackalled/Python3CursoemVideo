um = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
dois = ('onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

tres = um + dois
n = -1

while n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20: '))
print (tres[n])
