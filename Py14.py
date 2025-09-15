# fila deque hospital
# a direita serão inseridas pessoas com prioridade maior
# a esquerda atendimento básico


fila_atend = [None] * 6
qtd = 0

# add direita
def right_PrioPerson(paciente,qtd):
    if qtd == len(fila_atend):
        print('fila cheia')
    else:
        fila_atend[qtd] = paciente
        qtd = qtd + 1
        print('paciênte preferêncial inserido')

    return qtd

# remove direita
def atendPrio(qtd):
    pessoa = None
    if qtd == 0:
        print('fila vázia')
    else:
        pessoa = fila_atend[qtd-1]
        fila_atend[qtd-1] = None
        qtd = qtd - 1
        print('preferêncial atendido')
    return pessoa, qtd

# add esquerda
def leaf_personFast(paciente,qtd):
    if qtd == len(fila_atend):
        print('fila cheia')
    else:
        for i in range(qtd,0,-1): # em [qtd] começe do ultimo elemento [-1] e vá até o primeiro [0];
            fila_atend[i] = fila_atend[i -1] # desloque os valores para o final [-1];

        fila_atend[0] = paciente
        qtd = qtd + 1
        print('paciênte inserido')
    return qtd
# remove esquerda
def leaf(qtd):
    pessoa_1 = None
    if qtd == 0:
        print('fila vazia')
    else:
        pessoa_1 = fila_atend[0]
        for i in range(qtd-1):
            fila_atend[i] = fila_atend[i + 1]

        fila_atend[qtd-1] = None
        qtd = qtd - 1
        print('paciênte atendido')
    return pessoa_1, qtd

# (ATUALIZAR) - Fazer contagem de paciêntes preferências e não preferênciais ;

# acessar fila = opt_af
# atender_paciênte = opt_ap

while True:
    
    print('[0] - sair')
    print('[1] - acessar fila')
    print('[2] - atender paciênte')
    print('[3] - visualizar fila')
    
    opt = input('usuario>>:')

    if opt == '1':
        print('[1] - preferêncial')
        print('[2] - atendimento normal')

        opt_af = input('usuario>>:')

        if opt_af == '1':
            pref = input('paciente>>:')
            qtd = right_PrioPerson(pref,qtd)
        elif opt_af == '2':
            personFast = input('paciente>>:')
            qtd = leaf_personFast(personFast,qtd)
        else:
            print('opção ínvalida')

    elif opt == '2':
        print('[1] - atendimento preferêncial')
        print('[2] - atendimento rápido')

        opt_ap = input('usuario>>:')

        if opt_ap == '1':
            pessoa, qtd = atendPrio(qtd)
        elif opt_ap == '2':
            pessoa_1, qtd = leaf(qtd)
        else:
            print('opção ínvalida')

    elif opt == '3':
        print('fila atual:',fila_atend)

    elif opt == '0': # (ATUALIZAR) - Verificar se existem paciêntes na fila apois fechar o programa
        print('fim aplicação')
        break

    else:
        print('opção ínvalida')
        
