from random import randint
lista = []
jogos = []
print('-='*30)
print(' JOGO DA MEGA SENA  ')
print('-='*30)
quant = int(input('QUANTOS JOGOS VOCE QUER QUE EU SORTEIE? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-='*3, f'sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
