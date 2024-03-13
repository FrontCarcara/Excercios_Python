lista = []
dados = []
mai =  men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar?[S/N]:  '))
    if r in 'nN':
        break
    if r not in 'Ss':
        r = str(input('Digite uma resposta valida, tente novamente [S/N]:'))
print('-='*30)
print(f'Os dados cadastrados foram {lista}')
print(f'O total foram cadastrados {len(lista)} de pessoas')
print(f'O maior peso foi de {mai}kg, peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor foi de {men}kg, peso de ',end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}')
