print('{:=^40}'.format('Lojas FRONTELLI'))
preco = float(input('Preço das compras: '))
print(''' FORMAS DE PAGAMENTO!
[ 1 ]à vista dinheiro/cheque
[ 2 ]à vista cartão de débito
[ 3 ]2x no cartão de crédito
[ 4 ]3x ou mais no cartão de credito''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total =  preco - (preco * 10 / 100)
    print('Preço total com 10% de desconto = {:.2f}'.format(total))
if opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Preço total com 10% de desconto = {:.2f}'.format(total))
if opcao == 3:
    total = (preco / 2)
    print('Preço total parcelado em 2 vezes de = {:.2f}'.format(total))
if opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas?'))
    parce = total / parcelas
    print('Preço total com 20% de aumento em {} parcelas de = {:.1f}'.format(total, parce))
