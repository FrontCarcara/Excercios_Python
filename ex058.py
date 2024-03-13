from time import sleep
from random import randint
computador = randint(1, 10)
print('Carregando jogo de advinhação... pensarei em um numero de 1 a 10...')
for carregando in range(0, 3):
    print('pensando..')
    sleep(1)
print('Sera que você consegue advinhar qual foi?')
acertou = False
palpites = 0
valores = [1,2,3,4,5,6,7,8,9,10]
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    while jogador != int:
        jogador = int(input('Caracter errado, digite novamente!'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        elif jogador > computador:
            print('Menos.. tente mais uma vez')
print('Acertou!, foram tantas {} tentativas'.format(palpites))
