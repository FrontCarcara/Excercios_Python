
num = int(input('Digite um termo da sua PA:  '))
razao = int(input('Digite a razão:  '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print('{}'.format(c), end=' > ')
print('Acabou!')
