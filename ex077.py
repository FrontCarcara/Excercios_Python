
palavras = ("banana", "cachorro", "carro", "computador", "gato", "chave", "mesa", "livro", "telefone", "caneta")
for p in palavras:
    print(f'\nNa palavra{p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            