from  time import  sleep
def contador(i, f, p):
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.6)
            cont += p
        print('FIM!')
    else:
        cont = i
    while cont >= f:
        print(f'{cont} ', end='', flush=True)
        sleep(0.5)
        cont -= p
    print('FIM!')
contador(1, 10, 1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!: ')
ini = int(input('Inicio: '))
fim = int(input('Fim:  '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
