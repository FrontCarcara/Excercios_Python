num = int(input('Digite um termo da sua PA:  '))
razao = int(input('Digite a razão:  '))
termo = num
cont =  1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')