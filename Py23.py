'''Programa de lanchonete 
'''

# concluir

pedidos = [None] * 5
qtd = 0
concluido = 0
concluindo = 0

def inserir_pedido(pedido,qtd,concluido,concluindo):
    if qtd == len(pedidos):
        print('lista de pedidos cheia')
    else:
        if qtd != 0:
            concluindo = (concluindo + 1) % len(pedidos)

        pedidos[concluindo] = pedido
        qtd = qtd + 1
        
    return qtd,concluido,concluindo


def sair_pedido(qtd,concluido,concluindo):
    if (qtd == 0):
        print('lista de pedidos vazia')
    else:
        concluido = (concluido + 1) % len(pedidos)
        pedidos[concluido] = None
        qtd = qtd -1
        if qtd == 0:
            concluido = concluindo = 0

    return qtd, concluido, concluindo

while True:
    print('[0] - sair')
    print('[1] - inserir pedido')
    print('[2] - sair pedido')
    i = input('escolha>>:')
    if i == '1':
        
