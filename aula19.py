pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-='*30)
print(pessoas.keys())
print('-='*30)
print(pessoas.values())
print('-='*30)
print(pessoas.items())
print('-='*30)
pessoas['peso'] = 98
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)
brasil = []
estado1 = {'uf': 'Rio de janeiro', 'Sigla': 'Rj'}
estado2 = {'uf': 'São paulo', 'Sigla': 'Sp'}
brasil.append(estado2)
brasil.append(estado1)
print(brasil)
print('-='*30)
print(brasil[0]['uf'])
print('-='*30)
estado = dict()
brasil1 = list()
for c in range (0, 1 ):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil1.append(estado.copy())
print(brasil1)
print('-='*30)
for e in brasil1:
    for k1, v1 in e.items():
        print(f'O campo {k1} tem valor {v1}')
print('-='*30)
for e in brasil1:
    for v in e.values():
        print(v, end=' ')
    print()
print('-='*30)












