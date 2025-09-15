'''Sistema simples de loteria (sem fila prioritaria),
   que utiliza o método FIFO(First In, First Out).
'''

fila = [None] * 5
qtd = 0

def inserir(cliente,qtd):
    if qtd == len(fila):
        print('fila cheia')
    else:
        fila[qtd] = cliente
        qtd = qtd + 1
        print('cliente inserido')
    return qtd

def atender(qtd):
    pessoa = None
    if qtd == 0:
        print("fila vazia")
    else:
        pessoa = fila[0]
        for i in range(qtd-1):
            fila[i] = fila[i + 1]

        fila[qtd-1] = None
        qtd = qtd -1
        print('cliente atendido')
    return pessoa, qtd


while True:
    print("[0] - sair / [1] - add cliente / [2] - atender cliente")
    print(fila)
    opdd = input('escolha>>:')
    if opdd == '1':
        nome = input('nome do cliente>>:')
        qtd = inserir(nome,qtd)
    elif opdd == '2':
        pessoa, qtd = atender(qtd)
    elif opdd == '0':
        print('fim aplicação')
        break
    else:
        print('opção ínvalida')
