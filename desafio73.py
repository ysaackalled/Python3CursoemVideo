top10 = ('América-MG','Atlético-PR','Atlético-GO','Atlético-MG','Avaí','Botafogo','Ceará SC','Corinthians', 'Coritiba','Cuiabá')
top20 = ('Flamengo','Fluminense','Fortaleza','Goiás','Internacional','Juventude','Palmeiras','Bragantino','Santos','São Paulo')

tabela = (top10 + top20)
print('TABELA BRASILEIRÃO')
for pos, c in enumerate(tabela): # Tabela Inteira
    print(f'{pos+1}º: {tabela[pos]}')
print('-'*5)

print('TOP 5')
for c in range(0,6):
    print(f'{c+1}º: {tabela[c]}')
print('-'*5)

print('ZONA DE REBAIXAMENTO')
for c in range(len(tabela)-4, len(tabela)):
    print(f'{c+1}º: {tabela[c]}')
print('-'*5)

print('ORDEM ALFABÉTICA')
for c in range (0, len(tabela)):
    print(sorted(tabela)[c])
print('-'*5)

print(f'Posição do time FORTALEZA')
for c in range (0, len(tabela)):
    if 'fortaleza' in tabela[c].lower():
        print(f'O time Fortaleza está na {c+1}ª posição.')