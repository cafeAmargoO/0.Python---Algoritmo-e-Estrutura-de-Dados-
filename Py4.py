# FIla de banco

fila_banco = [None] * 8
clientes = 0
prox_cliente = 0
atender = 0

def inserir_cliente(cliente,clientes,prox_cliente,atender):
    if (clientes == len(fila_banco)):
        print('fila cheia')
    else:
        # se tiver mais de um valor no vetor
        if clientes != 0:
            # e ele não chegar ao final
            atender = (atender + 1) % (len(fila_banco))
        
        # acrescente em [atender] o próximo cliente a ser atendido
        fila_banco[atender] = cliente
        clientes = clientes + 1
        print('cliente inserido na fila')
        # se não tiver nenhum valor no vetor, o programa irá atender
        # o primeiro elemento do vetor

    return clientes, prox_cliente, atender

def atender_cliente(clientes,prox_cliente,atender):
    if (clientes == 0):
        print('fila vazia')
    else:
        # pegue o primeiro a ser atendido e remova
        fila_banco[prox_cliente] = None
        # e acrescente o próximo a ser atendido
        prox_cliente = (prox_cliente + 1) % len(fila_banco)
        # remove
        clientes = clientes - 1
        if clientes == 0:
            atender = prox_cliente = 0

    return clientes, prox_cliente, atender

while True:
    print('[0] - sair')
    print('[1] - inserir cliente')
    print('[2] - atender cliente')
    print('[3] - visualizar fila')

    operador = input('escolha:')

    if operador == '1':
        nome = input('nome do cliente:')
        clientes,prox_cliente,atender = inserir_cliente(nome,clientes,prox_cliente,atender)
        print(fila_banco)
        print('atender:',prox_cliente)
        print('próximo da fila:',atender)
    elif operador == '2':
        clientes,prox_cliente,atender = atender_cliente(clientes,prox_cliente,atender)
        print('cliente atendido')
        print(fila_banco)
        print('atender:',prox_cliente)
        print('próximo da fila:',atender)
    elif operador == '3':
        print(fila_banco)
        print('atender:',prox_cliente)
        print('próximo da fila:',atender)
    elif operador == '0':
        print('fila encerrada')
        print(fila_banco)
        print('atender:',prox_cliente)
        print('próximo da fila:',atender)
        break
    else:
        print('opção ínvalida')
