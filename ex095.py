time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
    if resp not in 'SN':
        print('ERRO! responda apenas com S ou N:')
        resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
    if resp == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    bus = int(input('Mostrar dados do jogador: (999 parar) '))
    if bus == 999:
        break
    if bus >= len(time):
        print(f'ERRO!não exite jogador com codigo {bus}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[bus]["nome"]}:')
        for i, g in enumerate(time[bus]['gols']):
            print(f'     No jogo {i+1} fez {g} gols. ')
print('<<  VOLTE SEMPRE  >>')


