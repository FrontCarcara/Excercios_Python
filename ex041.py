from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento:  '))
idade = atual - nascimento
if idade <= 9:
    print('{} anos é da categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('{} anos é da categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('{} anos é da categoria JUNIOR!'.format(idade))
elif idade <= 25:
    print('{} anos é da categoria SENIOR!'.format(idade))
else:
    print('{} anos é da categoria MASTER!'.format(idade))
