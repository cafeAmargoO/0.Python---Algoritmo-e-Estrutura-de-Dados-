fila_prio = [None] * 6
qtd = 0

def inserir(cliente,qtd):
    if qtd == len(fila_prio):
        print('fila cheia')
    else:
        fila_prio[qtd] = cliente
        qtd = qtd + 1
        print('cliente inserido na fila')
    return qtd

def remover(qtd):
    pessoa = None
    if qtd == 0:
        print('fila vazia')
    else:
        prio = False
        for i in range(qtd):
            if fila_prio[i][1] >= 65:
                prio = True
                ind_prio = i
                break

        if prio == True:
            pessoa = fila_prio[ind_prio]
            for i in range(ind_prio,qtd-1):
                fila_prio[i] = fila_prio[i + 1]

            fila_prio[qtd-1] = None
            qtd = qtd - 1

        else:
            pessoa = fila_prio[0]
            for i in range(qtd-1):
                fila_prio[i] = fila_prio[i + 1]

            fila_prio[qtd-1] = None
            qtd = qtd - 1

        return pessoa, qtd


while True:
    print('[0] - sair')
    print('[1] - inserir cliente')
    print('[2] - atender cliente')
    print('[3] - visualizar fila')
    last = input('opção:')
    if last == '1':
        nome = input('nome:')
        idade = int(input('idade:'))
        cliente = (nome, idade)
        qtd = inserir(cliente,qtd)
    elif last == '2':
        pessoa,qtd = remover(qtd)
    elif last == '3':
        print(fila_prio)
    elif last == '0':
        print('fim aplicação')
        print(fila_prio)
        break
    else:
        print('opção ínvalida')
