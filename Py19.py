''' Fila de pedidos de um restaurante
    utilizando uma fila circular
'''

pedidos = [None] * 12
qtd = 0

def inserir_pedido(pedido,qtd):
    if qtd == len(pedidos):
        print('fila cheia')
    else:
        pedidos[qtd] = pedido
        qtd = qtd + 1
        print('pedido adicionado')
    return qtd

def sair_pedido(qtd):
    sair = None
    if qtd == 0:
        print('sem pedidos na fila')
    else:
        sair = pedidos[0]
        for i in range(qtd-1):
            pedidos[i] = pedidos[i + 1]

        pedidos[qtd-1] = None
        qtd = qtd - 1
        print('pedido concluído')
    return sair, qtd

while True:
    print('[0] - sair')
    print('[1] - inserir pedido')
    print('[2] - sair pedido')
    print('[3] - visualizar pedidos')

    user = input('@usuario>>:')

    if user == '1':
        pedido = input('pedido>>:')
        qtd = inserir_pedido(pedido,qtd)
    elif user == '2':
        sair, qtd = sair_pedido(qtd)
    elif user == '3':
        print('pedidos:',pedidos)
    elif user == '0':
        if qtd > 0:
            print('Ainda há pedidos para sair')
            continue
        else:
            print('fim aplicação')
            break
    else:
        print('opção ínvalida')
