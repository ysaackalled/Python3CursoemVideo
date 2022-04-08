for c in range(0, 5):
    peso = float(input(f'{c+1}o peso: '))
    if c == 0: #adicionando o primeiro parametro para comparação
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'Maior peso: {maiorpeso}\nMenor peso: {menorpeso}')
