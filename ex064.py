n = cont = soma = 0
n = int(input('Digite um numero [999] para parar'))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero [999] para parar'))
print('voce digitou {} numeros e a soma foi {} entre eles.'.format(cont, soma))
