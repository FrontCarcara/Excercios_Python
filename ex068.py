from random import randint
v = 0
while True:
    computador =  randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    resultado = total % 2
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par (P) ou impar (i)?')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador jogou {computador}, Total de {total}')

    if tipo == 'P':
        if resultado == 0:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if resultado == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER!, Voce Conseguiu vencer {v}')

