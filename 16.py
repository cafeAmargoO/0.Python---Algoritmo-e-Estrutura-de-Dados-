''' Programa que compõe:
1>>:fila circular;
2>>:fila deque;
3>>:pilha;
4>>:fila prioritariao;
5>>:fila circular com prox, ult;

# objetivo:
 - Juntar vários tipos de dados de várias formas
   que o usuário desejar, os organizando em um
   vetor, do jeito que necessita o operador do
   programa;
'''

# fila circular - [fc];

fila_circular = [None] * 5
qtd_fc = 0

def inserir_dados(valor_fc,qtd_fc):
    if qtd_fc == len(fila_circular):
        print('fila cheia')
    else:
        fila_circular[qtd_fc] = valor_fc
        qtd_fc = qtd_fc + 1
        print('item adicionado')
    return qtd_fc

def remover_dados(qtd_fc):
    pessoa_fc = None
    if qtd_fc == 0:
        print('fila vazia')
    else:
        pessoa_fc = fila_circular[0]
        for i in range(qtd_fc-1):
            fila_circular[i] = fila_circular[i + 1]

        fila_circular[qtd_fc -1] = None
        qtd_fc = qtd_fc - 1
        print('item removido')
    return pessoa_fc, qtd_fc

# pilha - [pl];

pilha = [None]* 5
qtd_pl = 0

def empilhar(valor_pl,qtd_pl):
    if qtd_pl == len(pilha):
        print('fila cheia')
    else:
        pilha[qtd_pl] = valor_pl
        qtd_pl = qtd_pl + 1
        print('item adicionado a pilha')

    return qtd_pl

def desempilhar(qtd_pl):
    pessoa_pl = None
    if qtd_pl == 0:
        print('fila vazia')
    else:
        pessoa_pl = pilha[-1]
        pilha[qtd_pl -1] = None
        qtd_pl = qtd_pl - 1
        print('desempilhado')
    return pessoa_pl, qtd_pl

# fila deque

fila_deque = [None] * 5
qtd_dq = 0

# adição padrão (fila circular)
def inserir_direita(valor_dq,qtd_dq):
    if qtd_dq == len(fila_deque):
        print('fila cheia')
    else:
        fila_deque[qtd_dq] = valor_dq
        qtd_dq = qtd_dq + 1
        print('valor inserido na direita')
    return qtd_dq

# remoção pilha
def remover_direita(qtd_dq):
    pessoa_dq = None
    if qtd_dq == 0:
        print('fila vazia')
    else:
        pessoa_dq = fila_deque[-1]
        fila_deque[qtd_dq -1] = None
        qtd_dq = qtd_dq - 1
        print('item a direita removido')
    return pessoa_dq,qtd_dq

def inserir_esquerda(valor_dq,qtd_dq):
    if qtd_dq == len(fila_deque):
        print('fila cheia')
    else:
        for i in range(qtd_dq,0,-1): # começe no final do vetor[-1] e vá até o começo [0];
            fila_deque[i] = fila_deque[i -1] # apos isso, desloque os elementos para o final da lista[-1];

        fila_deque[0] = valor_dq
        qtd_dq = qtd_dq + 1
        print('valor inserido na esquerda')
    return qtd_dq

def remover_esquerda(qtd_dq):
    pessoa_dq0 = None
    if qtd_dq == 0:
        print('fila vazia')
    else:
        pessoa_dq0 = fila_deque[0]
        for i in range(qtd_dq -1):
            fila_deque[i] = fila_deque[i + 1]

        fila_deque[qtd_dq -1] = None
        qtd_dq = qtd_dq -1
        print('item a esquerda removido')
    return pessoa_dq0, qtd_dq

# fila prio

fila_prio = [None] * 5
qtd_prio = 0

def inserir_prio(valor_prio,qtd_prio):
    if qtd_prio == len(fila_prio):
        print('fila cheia')
    else:
        fila_prio[qtd_prio] = valor_prio
        qtd_prio = qtd_prio + 1
        print('inserido')
    return qtd_prio

def remover_prio(qtd_prio):
    sair_prio = None
    if qtd_prio == 0:
        print('fila vazia')
    else:
        prio = False
        for i in range(qtd_prio):
            if fila_prio[i][1] >= 65:
                prio = True
                ind_prio = i
                break
            
        if prio == True:
            sair_prio = fila_prio[ind_prio]
            for i in range(ind_prio,qtd_prio-1):
                fila_prio[i] = fila_prio[i + 1]
                
            fila_prio[qtd_prio -1] = None
            qtd_prio = qtd_prio - 1
            
        else:
            sair_prio = fila_prio[0]
            for i in range(qtd_prio-1):
                fila_prio[i] = fila_prio[i + 1]
                
            fila_prio[qtd_prio -1] = None
            qtd_prio = qtd_prio -1
            
    return sair_prio, qtd_prio
                
#def inserir

while True:
    print('[1] - Acessar métodos de adição de dados')
    print('[2] - visualizar todas as listas')
    print('[0] - sair')
    o = input('operador>>:')
    if o == '1':
        
        print('[1] - fila circular')
        print('[2] - pilha')
        print('[3] - fila deque')
        print('[4] - fila prioritária') # ausente
        
        a_mta = input('operador>>:')
        
        # fila circular;
        
        if a_mta == '1':
           print('fila circular:',fila_circular)
           print('[1] - inserir')
           print('[2] - remover')
           cod_fc = input('operador>>:')
           if cod_fc == '1':
              var_fc = input('>>:')
              qtd_fc = inserir_dados(var_fc,qtd_fc)
           elif cod_fc == '2':  
             pessoa_fc, qtd_fc = remover_dados(qtd_fc)
           else:
               print('opção ínvalida')
               
         # pilha;
               
        elif a_mta == '2':
           print('pilha:',pilha)
           print('[1] - empilhar')
           print('[2] - desempilhar')
           cod_pl = input('operador>>:')
           if cod_pl == '1':
               var_pl = input('>>:')
               qtd_pl = empilhar(var_pl,qtd_pl)
           elif cod_pl == '2':
               pessoa_pl,qtd_pl = desempilhar(qtd_pl)
           else:
               print('opção ínvalida')

        # fila deque
        
        elif a_mta == '3':
            print('fila deque:',fila_deque)
            print('[1] - inserir a direita da fila')
            print('[2] - inserir a esquerda da fila')
            print('[3] - remover direita')
            print('[4] - remover esquerda')

            cod_dq = input('operador>>:')
            if cod_dq == '1':
                var_dq = input('>>:')
                qtd_dq = inserir_direita(var_dq,qtd_dq)
            elif cod_dq == '2':
                var_dq = input('>>:')
                qtd_dq = inserir_esquerda(var_dq,qtd_dq)
            elif cod_dq == '3':
                pessoa_dq, qtd_dq = remover_direita(qtd_dq)
            elif cod_dq == '4':
                pessoa_dq0, qtd_dq = remover_esquerda(qtd_dq)
            else:
                print('opção ínvalida')
        # fila prio(incompleto)
        elif a_mta == '4':
            print('[1] - inserir dados')
            print('[2] - remover pessoa com idade maior de 65 anos')
            cod_prio = input('operador>>:')
            if cod_prio == '1':
                try:
                    var_prio = input('nome:')
                    var_prio1 = int(input('idade:'))
                    valor_prio = (var_prio,var_prio1)
                except ValueError:
                    print('idade deve ser inteiro')
            elif cod_prio == '2':
                qtd_prio, sair_prio = remover_prio(qtd_prio)
            else:
                print('opção ínvalida')
        else:
            print('opção ínvalida')
    # visualizo os dados guardados       
    elif o == '2':
        print('[1] - fila circular')
        print('[2] - fila deque')
        print('[3] - pilha')
        print('[4] - fila prioritaria')
        vs = input('>>:')
        if vs == '1':
            print('fila circular:',fila_circular)
        elif vs == '2':
            print('fila deque:',fila_deque)
        elif vs == '3':
            print('pilha:',pilha)
        elif vs == '4':
            print('fila prioritaria:',fila_prio)
        else:
            print('opção ínvalida')
            
    elif o == '0':
        print('exit')
        break
    else:
        print('opção ínvalida')
