total = totmil = cont = menor = 0
barato = ' '
while True:
    item = str(input('Qual item deseja comprar?')).strip()
    custo = float(input('Quanto custa?: R$'))
    total += custo
    cont += 1
    if custo > 1000:
        totmil += 1
    if cont == 1 or custo < menor:
        menor = custo
        barato = item
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('{=-=}' * 40)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00!')
print(f'O protudo mais barato foi {barato} que custa {menor:.2f}')