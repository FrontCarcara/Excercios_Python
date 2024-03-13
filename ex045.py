import random as rd
itens = ('pedra',  'papel,', 'tesoura')
computador = rd.randint(0, 2)
jogador = int(input('''Escolha sua opção:
0 = pedra
1 = tesoura
2 = papel
'''))
print('O computador escolheu {}!'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('o jogo deu EMPATE')
    elif jogador == 1:
        print('o COMPUTADOR ganhou!')
    elif jogador == 2:
        print('parabens VOCÊ ganhou!')
    else:
        print('JOGADA IVALIDA!') #computador jogou tesoura
elif computador == 1:
    if jogador == 0:
        print('parabens VOCÊ ganhou!')
    elif jogador == 1:
        print('o jogo deu EMPATE')
    elif jogador == 2:
        print('o COMPUTADOR ganhou!')
    else:
        print('JOGADA IVALIDA!')
elif computador == 2:  #computador jogou papel
    if jogador == 0:
        print('o COMPUTADOR ganhou!')
    elif jogador == 1:
        print('parabens VOCÊ ganhou!')
    elif jogador == 2:
        print('o jogo deu EMPATE')
    else:
        print('JOGADA IVALIDA!')
else:
    print('JOGADA IVALIDA!')