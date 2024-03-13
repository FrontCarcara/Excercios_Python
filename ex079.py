x = []
while True:
    n = int(input('Digite um valor: '))
    if n not in x:
        x.append(n)
        print('VALOR ADICIONADO!')
    else:
        print('Valor duplicado, não vou adicicionar..')
    r =  str(input('Quer continuar? [S/N]:'))
    if r in 'Nn':
        break
print('-='*30)
x.sort()
print(f'Você digitou os valores {x}')