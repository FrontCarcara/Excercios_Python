num = (int(input('Digite um numero: '))
       ,int(input('Digite um numero: '))
       ,int(input('Digite um numero: '))
       ,int(input('Digite um numero: ')))
print(f'Você digitou os valores {num} ')
print(f'Você digitou o valor 9, {num.count(9)} vezes')
if 3 in num:
    print(f'Você digitou o valor na {num.index(3)+1} posição ')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 ==0:
        print(n, end= ' ')