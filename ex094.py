pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] =str(input('Nome: '))
    while True:
        pessoa['sexo'] =str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'Opss, carater invalido, digite novamente[M/F]')
        pessoa['sexo'] =str(input('Sexo: [M/F]')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!, Responda apenas com S ou N [S/N]: ')
    if resp == 'N':
        break
print('-='*30)
print(galera)
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ', end='')
print()
print('Pessoas que estão acima da media:', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
print('< < ENCERRADO > >')