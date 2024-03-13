altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2
print('seu IMC é igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('você esta abaixo do peso!')
elif imc <= 25:
    print('Voce esta com o peso ideal!')
elif imc <= 30:
    print('Voce esta sobrepeso!')
elif imc <=40:
    print('voce esta com obesidade!')
elif imc > 40:
    print('Você com obesidade morbida!')
