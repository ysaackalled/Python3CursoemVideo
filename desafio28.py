from random import randint

n = int(input('Digite um número entre 0 e 5: '))
npc = randint(0,5)

if (n == npc):
    print('Você acertou!')
else:
    print('Você errou. O número escolhido foi {}.'.format(npc))
    if (n == npc + 1 or n == npc -1):
        print('Quase acertou!')
    
    

