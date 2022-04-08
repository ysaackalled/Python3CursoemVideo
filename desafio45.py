from random import randint
ppt = int(input('Vamos jogar pedra, papel e tesoura. Escolha uma opção: \n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3*] Tesoura\n'))
vcarma = ''

if ppt == 1:
    vcarma = 'pedra'
elif ppt == 2:
    vcarma = 'papel'
else:
    vcarma = 'tesoura'

print(f'Você escolheu {vcarma}!')
pc = randint(1,3)
pcarma = ''

if pc == 1:
    pcarma = 'pedra'
elif pc == 2:
    pcarma = 'papel'
else:
    pcarma = 'tesoura'

print(f'O computador escolheu {pcarma}!')

if vcarma == pcarma:
    print('Empate!')
elif (vcarma == 'pedra' and pcarma == 'papel') or (vcarma == 'papel' and pcarma == ' tesoura') or (vcarma == 'tesoura' and pcarma == 'pedra'):
    print('Você perdeu!')
else:
    print('Você venceu!')