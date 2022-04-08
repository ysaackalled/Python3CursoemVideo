n = int(input('Digite os números a serem somados:\n'))
if n != 999:
    soma = n
    termos = 1
else:
    soma = 0
    termos = 0
while n != 999:
    n = int(input()) 
    if n == 999:
        break
    else:
        soma += n
        termos += 1       
print(f'A soma é {soma}, foram digitados {termos} números.')
