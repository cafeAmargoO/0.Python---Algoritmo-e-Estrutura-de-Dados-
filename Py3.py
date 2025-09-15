'''Fazendo uma fila deque de forma iterativa
'''

fila_deque = [None] * 5
qtd = 0

# inserir

def inserir_direita(valor,qtd):
    if qtd == len(fila_deque):
        print('fila cheia')
    else:
        fila_deque[qtd] = valor
        qtd = qtd + 1

    return qtd

def inserir_esquerda(valor,qtd):
    if qtd == len(fila_deque):
        print('fila cheia')
    else:
        for i in range(qtd, 0, -1):
            fila_deque[i] = fila_deque[i -1]

        fila_deque[0] = valor
        qtd = qtd + 1

    return qtd

# remover

def remover_direita(qtd):
    remover_direita = None
    if qtd == 0:
        print('fila vazia')
    else:
        remover_direita = fila_deque[-1]
        fila_deque[qtd-1] = None
        qtd = qtd - 1

    return remover_direita, qtd

def remover_esquerda(qtd):
    remover_esquerda = None
    if qtd == 0:
        print('fila vazia')
    else:
        remover_esquerda = fila_deque[0]
        for i in range(qtd-1):
            fila_deque[i] = fila_deque[i + 1]

        fila_deque[qtd-1] = None
        qtd = qtd - 1

    return remover_esquerda, qtd

while True:
    print('[0] - sair')
    print('[1] - acessar fila')
    print('[2] - remover')
    print('[3] - ver lista')

    user_o = input('opção:')

    # adicionar
    if user_o == '1':
        print(fila_deque)
        print('[1] - sim | [0] - não')
        user_t = input('deseja adicionar um elemento?')
        if user_t == '1':
            print('[1] - direita | [2] - esquerda')
            choice_order = input('deseja adicionar a direita ou esquerda da fila?:')
            if choice_order == '1':
                elemento_direita = input('digite o elemento que deseja armazenar:')
                qtd = inserir_direita(elemento_direita,qtd)
            elif choice_order == '2':
                elemento_esquerda = input('digite o elemento que deseja armazenar:')
                qtd = inserir_esquerda(elemento_esquerda,qtd)
            else:
                print('opção ínvalida')
        elif user_t == '0':
            continue
        else:
            print('opção ínvalida')

    # remover
    elif user_o == '2':
        print(fila_deque)
        print('[1] - remover elemento direito')
        print('[2] - remover elemento esquerdo')
        user_tr = input('opção:')
        if user_tr == '1':
            remover_direita = remover_direita(qtd)
        elif user_tr == '2':
            remover_esquerda = remover_esquerda(qtd)
        else:
            print('opção ínvalida')
    elif user_o == '3':
        print(fila_deque)
    elif user_o == '0':
        print('fim aplicação')
        break
    else:
        print('opção ínvalida')
