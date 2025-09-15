# fila de festa com prioridade

fila = [None] * 6
qtd = 0
loop = True

def inserir_fila(cliente,qtd):
    if qtd == len(fila):
        print('fila cheia')
    else:
        fila[qtd] = cliente
        qtd = qtd + 1
        print('inserido na fila')
    return qtd

def entrada(qtd):
    pessoa = None
    if qtd == 0:
        print('fila vazia')
    else:
        prio = False
        for i in range(qtd):
            if fila[i][1] == 'VIP'.upper():
                prio = True
                vip = i
                break

        if prio == True:
            pessoa = fila[vip]
            for i in range(vip,qtd-1):
                fila[i] = fila[i + 1]

            fila[qtd-1] = None
            qtd = qtd - 1
            print('acesso liberado')
        else:
            pessoa = fila[0]
            for i in range(qtd-1):
                fila[i] = fila[i + 1]

            fila[qtd-1] = None
            qtd = qtd - 1
            print('acesso liberado')
    return pessoa, qtd

while loop:
    print('[0] - sair')
    print('[1] - inserir pessoa na fila')
    print('[2] - entrada')
    print('[3] - visualizar fila')

    opt = input('escolha:')
    if opt == '1':
        nome = input('nome:')
        tipo_entrada = input('tipo de entrada:').upper()
        cliente = (nome,tipo_entrada)
        qtd = inserir_fila(cliente,qtd)
    elif opt == '2':
        pessoa, qtd = entrada(qtd)
    elif opt == '3':
        print('fila atual:',fila)
    elif opt == '0':
        print('fila atual:',fila)
        loop = False
    else:
        print('opção ínvalida')
            
        
