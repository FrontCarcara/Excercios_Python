print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você deseja sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        total += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
