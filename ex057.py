sexo = str(input('Informe o seu SEXO: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. por favor. informe o seu sexo corretamente!:  ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('Sexo {} resgistrado com secesso'.format(sexo))
