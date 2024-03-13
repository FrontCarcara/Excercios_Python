num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
opçao = 0
while opçao != 5:
    print('''
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair''')
    opçao = int(input('Qual é sua opção: '))
    if opçao == 1:
        soma = num1 + num2
        print('A soma de {} e {} é igual a {}'.format( num1, num2, soma))
    elif opçao == 2:
        mult = num1 * num2
        print('A multiplicação de {} e {} é igual a {}'.format(num1, num2, mult))
    elif opçao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
    elif opçao == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('finalizando..')
    else:
        print('opçao invalida, tente novamente')
    print('=-=' * 10)
print('Fim do programa!')
