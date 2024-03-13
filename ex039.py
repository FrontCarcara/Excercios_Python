from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento:  '))
idade = atual -  nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos, faltam ainda {} anos para se alistar!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('VocE ja deveria ter se alistado a {} anos!'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
