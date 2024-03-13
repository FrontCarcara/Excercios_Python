def mult(a, b):
    m = a * b
    print(f'LARGURA (M): {a}')
    print(f'COMPRIMENTO (m): {b}')
    print(f'A Area do terreno é igual a {a} X {b} = {m}M²')
def lin():
    print('-'*40)


a = float(input('Digite a LARGURA: '))
b = float(input('Digite o COMPRIMENTO: '))

print('Controle de Terrenos')
lin()
mult(a, b)
lin()