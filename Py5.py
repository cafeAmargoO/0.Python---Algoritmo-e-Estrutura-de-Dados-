# caixa de arquivos
# pilha

caixa = [None] * 8
arquivos = 0

def arquivar(arquivo,arquivos):
    if arquivos == len(caixa):
        print('caixa cheia')
    else:
        caixa[arquivos] = arquivo
        arquivos = arquivos + 1
        print('item arquivado')

    return arquivos

def desarquivar(arquivos):
    remover = None
    if arquivos == 0:
        print('caixa vazia')
    else:
        remover = caixa[arquivos-1]
        caixa[arquivos-1] = None
        arquivos = arquivos - 1
        print('item desarquivado')

    return remover, arquivos

while True:
    print('[0] - fechar')
    print('[1] - guarda arquivo')
    print('[2] - remover arquivo')
    print('[3] - visualizar arquivos')

    last = input('opção:')

    if last == '1':
        item = input('nome do item:')
        arquivos = arquivar(item,arquivos)
    elif last == '2':
        remover,arquivos = desarquivar(arquivos)
    elif last == '3':
        print(caixa)
    elif last == '0':
        print('fim aplicação')
        print(caixa)
        break
    else:
        print('opção ínvalida')
        
        
