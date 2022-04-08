homens = 0
contamulher = 0
demaior = 0

while True:
    nome = str(input('Digite um nome: '))
    sexo = str(input(f'Qual o sexo de {nome} (m/f)? ').upper())
    idade = int(input(f'Qual a idade de {nome}? '))
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        contamulher += 1
    if idade >= 18:
        demaior += 1
    continua = str(input('Deseja continuar(s/n)? ').upper())
    if continua == 'N':
        break
    
print(f'A ) Pessoas com +18 anos: {demaior}')
print(f'B ) Homens cadastrados: {homens}')
print(f'C ) Mulheres com -20 anos: {contamulher}')