from random import randint
pc = randint(0, 10)
vc = int(input('Tente adivinhar o número escolhido (0 à 10): '))
palpite = 1
while vc != pc:
    palpite += 1
    vc = int(input('Tente novamente: '))
print(f'Você acertou! Foram necessários {palpite} palpites.')
