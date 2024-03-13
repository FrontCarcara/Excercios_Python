maior_idade = menor_20 = homens = 0
while True:
    idade = int(input('Qual a idade desta pessoa?: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()[0]
    resp = ' '
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menor_20 += 1
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'ao todos temos {menor_20} mulheres com menos de 20 anos!')
print(f'Temos no total {homens} homens!')
print('Acabou!')
