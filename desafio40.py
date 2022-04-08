nota1 = float(input('Digite a 1a nota: '))
nota2 = float(input('Digite a 2a nota: '))
nota = (nota1+nota2) / 2

if (nota < 5):
    print('Reprovado!')
elif (nota >= 7):
    print('Aprovado!')
else:
    print('Recuperação!')