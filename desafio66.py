n = soma = num =0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    num += 1

print(f'A soma entra os números é {soma} e foram digitados {num} numeros.')
