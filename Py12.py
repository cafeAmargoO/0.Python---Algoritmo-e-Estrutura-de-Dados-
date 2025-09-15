#fila loteria simples

fila = [None] * 5
qtd = 0

def inserir(npc,qtd):
    if qtd == len(fila):
        print('fila cheia')
    else:
        fila[qtd] = npc
        qtd = qtd + 1
        print('cliente inserido na fila')
    return qtd

def remover(qtd):
    pessoa = None
    if qtd == 0:
        print('fila vazia')
    else:
        pessoa = fila[0]
        for i in range(qtd-1):
            fila[i] = fila[i + 1]

        fila[qtd-1] = None
        qtd = qtd - 1
        print('cliente atendido')
    return pessoa, qtd

while True:
    print('[0] - sair')
    print('[1] - inserir cliente')
    print('[2] - atender cliente')
    print('[3] - visualizar fila')

    opt = input('escolha:')

    if opt == '1':
        nome = input('nome do cliente:')
        qtd = inserir(nome,qtd)
    elif opt == '2':
        pessoa, qtd = remover(qtd)
    elif opt == '3':
        print(fila)
    elif opt == '0':
        print('fila atual:',fila)
        break
    else:
        print('opção ínvalida')
        
