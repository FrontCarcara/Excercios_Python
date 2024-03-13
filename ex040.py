num1 = float(input('Digite a primeira nota:   '))
num2 = float(input('Digite a segundo nota:   '))
media = (num1 + num2) / 2
print('Sua média foi {}!'.format(media))
if media < 5.0:
    print('REPROVADO')
elif media > 7.0:
    print('APROVADO')
else:
    print('RECUPERAÇÂO')
