lista = []
for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os Valores digitados foram: {lista}, e ela tem {len(lista)} valores.')
maior = max(lista)
posiçao_maior = lista.index(maior)
menor = min(lista)
posiçao_menor = lista.index(menor)
print(f' o Maior valor digitado foi {maior} e ele esta na posição {posiçao_maior+1}')
print(f' E o menor valor digitado foi {menor} e a sua posição foi {posiçao_menor+1}.')

