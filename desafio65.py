soma = 0
c = int(input('Digite números para obter a média entre eles(999 p/ parar):\n'))
maior = c
menor = c
termos = 1

while c != 999:
    soma += c
    c = int(input())
    if c != 999:
        termos += 1
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        media = soma / termos
        
print(f'Média: {media:.1f}\nMaior: {maior}\nMenor: {menor}')
  
if c == 999:
    print('FIM!')
