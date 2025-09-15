fila = [None] * 3
qtd = 0

def inserir(valor,qtd):
    if qtd == len(fila):
        print('fila cheia')
    else:
        fila[qtd] = valor
        qtd = qtd + 1

    return qtd

def remover(qtd):
    pessoa = None
    if qtd == 0:
        print('lista vazia')
    else:
        pessoa = fila[0]
        for i in range(qtd-1):
            fila[i] = fila[i + 1]

        fila[qtd-1] = None
        qtd = qtd - 1


    return pessoa, qtd


while True:
    print('[0] - sair')
    print('[1] - adicionar cliente')
    print('[2] - remover cliente')
    print('[3] - visualizar a fila')

    user = input('opção:')

    if user == '1':
        nome = input('digite o nome do cliente:')
        qtd = inserir(nome,qtd)
        print(fila)
    elif user == '2':
        pessoa, qtd = remover(qtd)
    elif user == '3':
        print(fila)
    elif user == '0':
        print('programa encerrado')
        print('fila atual:',fila)
        break
    else:
        print('opção ínvalida')
    
            
