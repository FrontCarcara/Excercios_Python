listagem =  ('lapis', 1.75,
             'borracha', 2,
             'caderno' , 15.90,
             'Estojo', 25,
             'transferidor', 4.20,
             'Compasso', 9.90)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
