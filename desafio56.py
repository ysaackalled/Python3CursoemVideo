somaidade = 0
maxidade = 0
m20 = 0

for c in range(0, 4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(H ou M): ')).lower()
    somaidade += idade
    
    if (idade > maxidade) and (sexo == 'h'): #NOME E IDADE DO MAIS VELHO
        maxidade = idade
        nomevei = nome

    if (idade < 20) and (sexo == 'm'): #QUANTIDADE DE MULHERES COM MENOS DE 20
        m20 += 1

media = somaidade / (c+1)
print(f'A média de idade é: {media:.1f}')
print(f'O homem mais velho é {nomevei} com {maxidade} anos.')
print(f'No grupo há {m20} mulheres com menos de 20 anos.')
