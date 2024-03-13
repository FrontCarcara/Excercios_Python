lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('VALOR ADICIONADO!..')
    r = str(input('DESEJA CONTINUAR? [S/N]:'))
    if r in 'Nn':
        break
    if r not in 'Ss':
        print('RESPOSTA INVALIDA!, Tente novamente!')
        r = str(input('DESEJA CONTINUAR? [S/N]: '))
print(f'A lista teve {len(lista)} itens!')
lista.sort(reverse=True)
print(f'a lista tem os valores {lista}')
contador = 0
for valor in lista:
    if valor == 5:
        contador += 1
print(f' o valor 5 aparece : {contador}, vezes na lista!')

