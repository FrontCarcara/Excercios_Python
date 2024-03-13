from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for n in range(0, 6):
    nasc = int(input('Digite o ano em que a pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} maiores de idade'.format(totmaior))
print('{} menores de idade'.format(totmenor))
