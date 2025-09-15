# pilha de arquivos
fila=[None] * 3
qtd = 0

def inserir_arquivo(file,qtd):
    if qtd == len(fila):
        print('pilha cheia')
    else:
        fila[qtd] = file
        qtd = qtd + 1
        print("arquivo inserido")
    return qtd

def remover_arquivo(qtd):
    arquivo = None
    if qtd == 0:
        print('pilha vázia')
    else:
        arquivo = fila[-1]
        fila[qtd-1] = None
        qtd = qtd - 1
        print('arquivo removido')
    return arquivo, qtd

while True:
    print('[0] - sair')
    print('[1] - guardar arquivo')
    print('[2] - retirar arquivo')
    print('[3] - visualizar pilha')

    opt = input('usuario>>:')

    if opt == '1':
        name_file = input('nome_arquivo>>:')
        qtd = inserir_arquivo(name_file,qtd)
    elif opt == '2':
        arquivo, qtd = remover_arquivo(qtd)
    elif opt == '3':
        print(fila)
    elif opt == '0':
        print('fim aplicação')
        break
    else:
        print('opção ínvalida')
