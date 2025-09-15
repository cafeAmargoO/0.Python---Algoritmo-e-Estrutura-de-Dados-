# fila de show pop

fila_entrada = [None] * 5
pessoas = 0
loop = True

def chegada(pessoa,pessoas):
    if pessoas == len(fila_entrada):
        print('fila cheia')
    else:
        fila_entrada[pessoas] = pessoa
        pessoas = pessoas + 1
        print('cliente inserido na fila')
    return pessoas

def acesso(pessoas):
    entrada = None
    if pessoas == 0:
        print('fila vazia')
    else:
        entrada = fila_entrada[0]
        for i in range(pessoas-1):
            fila_entrada[i] = fila_entrada[i + 1]

        fila_entrada[pessoas-1] = None
        pessoas = pessoas - 1
        print('acesso liberado')
    return entrada, pessoas

while loop:
    print('[0] - sair')
    print('[1] - inserir cliente na fila')
    print('[2] - liberar acesso')
    print('[3] - visualizar fila')

    final = input('escolha:')

    if final == '1':
        nome = input('nome:')
        pessoas = chegada(nome,pessoas)
    elif final == '2':
        entrada, pessoas = acesso(pessoas)
    elif final == '3':
        print(fila_entrada)
    elif final == '0':
        print('fila atual:',fila_entrada)
        loop = False
    else:
        print('opção ínvalida')



        
