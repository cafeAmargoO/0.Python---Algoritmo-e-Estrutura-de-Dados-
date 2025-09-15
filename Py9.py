# fila de banco com prioridade

fila_banco = [None] * 8
clientes = 0
loop = True

def inserir_cliente(cliente,clientes):
    if clientes == len(fila_banco):
        print('fila cheia')
    else:
        fila_banco[clientes] = cliente
        clientes = clientes + 1
        print('cliente inserido na fila')
    return clientes

def atender_cliente(clientes):
    pessoa = None
    if clientes == 0:
        print('fila vazia')
    else:
        prio = False
        for i in range(clientes): 
            if fila_banco[i][1] >= 65:
                prio = True
                ind_prio = i
                break
        if prio == True:
            pessoa = fila_banco[ind_prio]
            for i in range(ind_prio,clientes-1): 
                fila_banco[i] = fila_banco[i + 1]

            fila_banco[clientes-1] = None
            clientes = clientes - 1
            print('cliente atendido')
        else:
            pessoa = fila_banco[0]
            for i in range(clientes-1):
                fila_banco[i] = fila_banco[i + 1]

            fila_banco[clientes-1] = None
            clientes = clientes - 1
            print('cliente atendido')
            
    return pessoa, clientes

while loop:
    print('[0] - sair')
    print('[1] - adicionar cliente')
    print('[2] - atender cliente')
    print('[3] - visualizar fila')

    last = input('escolha:')

    if last == '1':
        nome = input('nome:')
        idade = int(input('idade:'))

        cliente = (nome, idade)
        clientes = inserir_cliente(cliente,clientes)
    elif last == '2':
        pessoa, clientes = atender_cliente(clientes)
    elif last == '3':
        print('fila atual:',fila_banco)
    elif last == '0':
        print('fila atual:',fila_banco)
        loop = False
    else:
        print('opção ínvalida')
