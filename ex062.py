ep = '=-=' * 10
num = int(input('Digite um termo da sua PA:  '))
print(ep)
razao = int(input('Digite a razão:  '))
print(ep)
termo = num
cont =  1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? / Digite ''0'' para encerrar '))
print('PA finalizada com {} termos mostrados'.format(total))
print(ep)
print('FIM')