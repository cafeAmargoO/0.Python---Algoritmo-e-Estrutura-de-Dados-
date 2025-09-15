# fila de loja de eletronicos

fila_caixa = [None] * 8
clientes = 0
loop = True

def fila(cliente,clientes):
    if clientes == len(fila_caixa):
        print('fila cheia')
    else:
        fila_caixa[clientes] = cliente
        clientes = clientes + 1
        print('cliente inserido na fila')
        
    return clientes

def atender_cliente(clientes):
    atender = None
    if clientes == 0:
        print('fila vazia')
    else:
        atender = fila_caixa[0]
        for i in range(clientes-1):
            fila_caixa[i] = fila_caixa[i + 1]

        fila_caixa[clientes-1] = None
        clientes = clientes  - 1
        print('cliente atendido')
        
    return atender, clientes

while loop:
    print('[0] - sair')
    print('[1] - inserir cliente na fila')
    print('[2] - atender cliente')
    print('[3] - visualizar fila')

    final = input('escolha:')

    if final == '1':
        nome = input('nome:')
        clientes = fila(nome,clientes)
    elif final == '2':
        atender, clientes = atender_cliente(clientes)
    elif final == '3':
        print(fila_caixa)
    elif final == '0':
        print('fila atual:',fila_caixa)
        loop = False
    else:
        print('opção ínvalida')
