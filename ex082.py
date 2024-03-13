lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    r = str(input('DESEJA CONTINUAR? [S/N]: '))
    if r in 'nN':
        break
    if r not in 'Ss':
        print('RESPOSTA INVALIDA, TENTE NOVAMENTE..')
print(lista,'lista')
print(lista_par,'par')
print(lista_impar,'impar')