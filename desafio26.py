frase = input('Digite uma frase: ')
cont = frase.upper().count('A')
prima = (frase.upper().find('A') + 1)
ultima = (frase.upper().rfind('A') + 1)
print('A letra A aparece {} vezes.'.format(cont))
print('Ela aparece a primeira vez na casa {}.'.format(prima))
print('Ela aparece a ultima vez na casa {}.'.format(ultima))