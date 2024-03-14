import time
from random import randint
from time import sleep
def sortear(lista):
    print('Sorteando valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        time.sleep(0.5)
    print('PRONTO')
numeros = list()

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')




sortear(numeros)
somaPar(numeros)


