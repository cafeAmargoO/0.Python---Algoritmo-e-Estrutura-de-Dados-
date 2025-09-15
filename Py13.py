# o método de inserir dados a esquerda e direita de uma fila
# utilizamos uma pilha, para remover itens a direita, e fila circular
# para remover itens a esquerda;

# para adicionar a direita se utiliza o método padrão de adição
# já a esquerda, utilizamos deslocamente de elementos;

# o nome do método chamado é fila deque;

fila_deque = [None] * 6
qtd = 0

# 1- Direita

# adição padrão

def inserir_direita(valor,qtd):
    if qtd == len(fila_deque):
        print('fila cheia')
    else:
        fila_deque[qtd] = valor
        qtd = qtd + 1
        print('inserido a direita da fila')
    return qtd

# pilha

def remover_direita(qtd):
    pessoa = None
    if qtd == 0:
        print('fila vazia')
    else:
        pessoa = fila_deque[qtd -1]
        fila_deque[qtd -1] = None
        qtd = qtd - 1
        print('item a direita removido')
    return pessoa, qtd

# 2 - Esquerda

def inserir_esquerda(valor,qtd):
    if qtd == len(fila_deque):
        print('fila cheia')
    else:
        for i in range(qtd, 0, -1): # começo de -1(último elemento), e vou até 0(primeiro elemento);
            fila_deque[i] = fila_deque[i -1] # desloco todos os elementos para o final da fila

        fila_deque[0] = valor # assim, abrindo espaço para inserir o valor a esquerda
        qtd = qtd + 1
        print('inserido a esquerda da fila')
    return qtd

# método de remoção de uma fila circular
def remover_esquerda(qtd):
    pessoa1 = None
    if qtd == 0:
        print('fila vazia')
    else:
        pessoa1 = fila_deque[0]
        for i in range(qtd-1):
            fila_deque[i] = fila_deque[i + 1]

        fila_deque[qtd-1] = None
        qtd = qtd - 1
        print('item a esquerda removido')
    return pessoa1, qtd

while True:
    print('Fila onde pode ser ínserido valores a esquerda, e a direita da lista')
    print('[0] - sair')
    print('[1] - inserir a direita')
    print('[2] - inserir a esquerda')
    print('[3] - remover a direita')
    print('[4] - remover a esquerda')
    print('[5] - visualizar fila')

    opt = input('usuário>>:')

    if opt == '1':
        my_var = input('nome>>:')
        qtd = inserir_direita(my_var,qtd)
    elif opt == '2':
        my_var1 = input('nome>>:')
        qtd = inserir_esquerda(my_var1,qtd)
    elif opt == '3':
        pessoa, qtd = remover_direita(qtd)
    elif opt == '4':
        pessoa, qtd = remover_esquerda(qtd)
    elif opt == '5':
        print('fila atual:',fila_deque)
    elif opt == '0':
        print('fim aplicação')
        print('itens na fila:',fila_deque)
        break
    else:
        print('opção ínvalida')
