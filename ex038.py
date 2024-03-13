num1 = int(input('Digite o primeiro numero:   '))
num2 = int(input('Digite o segundo numero:    '))
if num1 > num2:
    print('O primeiro numero ({}) é MAIOR que o segundo numero ({})'.format(num1, num2))
elif num2 > num1:
    print('O segundo numero ({}) é maior que o primeiro numero ({})'.format(num2,num1))
elif num1 == num2:
    print('Ambos os valores são iguais! primeiro {} == segundo {}'.format(num1,num2))
else: print('Valor incorreto, tente novamente!')
