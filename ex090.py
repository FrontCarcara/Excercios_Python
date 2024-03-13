aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'recuperação'
else:
    aluno['situaçao'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')