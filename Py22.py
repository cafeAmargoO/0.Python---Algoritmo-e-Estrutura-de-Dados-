'''Este algoritmo recebe processos de um tribunal, mostra
   a quantidade processos a serem atendidos e a quantidade de
   novos espaços para processos futuros, utilizando uma fila circular'''


processos = [None] * 5
qtd = 0
novo_proc = 0
prox_proc = 0

def inserir_processo(processo,qtd,novo_proc,prox_proc):
    if qtd == len(processos):
        print('fila de processos cheia')
    else:
        if qtd != 0: # se já tiver algum item no índice 0
            prox_proc = (prox_proc + 1) % len(processos) # percorra este contador até o final do array

        processos[prox_proc] = processo
        qtd = qtd + 1
        print('processo inserido')
    return qtd, novo_proc, prox_proc

def atender_processo(qtd, novo_proc, prox_proc):
    if (qtd == 0):
        print('fila vazia')
    else:
        processos[novo_proc] = None
        novo_proc = (novo_proc + 1) % len(processos)
        qtd = qtd - 1
        print('processo atendido')
        if qtd == 0:
            novo_proc = prox_proc = 0
    return qtd, novo_proc, prox_proc

while True:
    print('[0] - sair')
    print('[1] - inserir processo')
    print('[2] - atender processo')
    print(processos)
    print('Processos em andamento:',prox_proc)
    print('processos novos:',novo_proc)
    i=input('@usuario>>:')
    if i == '1':
        nome=input('nome do processo>>:')
        qtd, novo_proc, prox_proc = inserir_processo(nome, qtd, novo_proc, prox_proc)
    elif i == '2':
        qtd, novo_proc, prox_proc = atender_processo(qtd, novo_proc, prox_proc)
    elif i == '0':
        print('fim aplicação')
        break
    else:
        print('opção ínvalida')
        
