peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt * alt)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, voce está abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é de {imc:.2f}, você está no peso ideal.')
elif imc < 30:
    print(f'Seu IMC é de {imc:.2f}, voce está no sobrepeso.')
elif imc < 40:
    print(f'Seu IMC é de {imc:.2f}, você está na obesidade.')
else:
    print(f'Seu IMC é de {imc:.2f}, você está na obesidade mórbida')