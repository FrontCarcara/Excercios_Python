n = cont = soma = quant = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros e a media foi: {}'.format(quant, media))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))
