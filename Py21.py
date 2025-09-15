'''Programa que verifica próximo paciênte a ser atendido,
   e conta a quantidade de paciêntes que estão na fila;

   PS: Utiliza-se fila circular
'''

fila=[None] * 4
qtd = 0
primeiro_atend = 0
prox_atend = 0

def validar_nome(nome):
    if not nome or nome.strip() == '':
        print('erro: o espaço não pode ficar vázio')
        return False
    if nome.isdigit():
        print('erro: não deve ter números no nome')
        return False
    return True

def add_paciente(paciente,qtd,primeiro_atend,prox_atend):
    if qtd == len(fila):
        print('fila cheia')
    else:
        if qtd != 0:
            prox_atend = (prox_atend + 1) % len(fila) # garante a fila circular, apartir do índice [1] paciente é adicionado há [prox_atend]

        fila[prox_atend] = paciente
        qtd = qtd + 1
        print('paciênte inserido')
    return qtd, primeiro_atend, prox_atend

def atender(qtd,primeiro_atend,prox_atend):
    if (qtd == 0):
        print('fila vaiza')
    else:
        fila[primeiro_atend] = None
        primeiro_atend = (primeiro_atend + 1) % len(fila) # quando removido, o número de vagas que vão ficando disponível vão crescendo
        qtd = qtd - 1
        print('paciênte atendido')
        if qtd == 0:
            primeiro_atend = prox_atend = 0 # caso a fila fique zerada, o contador é zerado
    return qtd, primeiro_atend, prox_atend

while True:
    print('[0] - sair')
    print('[1] - inserir paciênte')
    print('[2] - atender paciênte')
    print(fila)
    print('próximo atendimento:',primeiro_atend)
    print('aguardando na fila:',prox_atend)
    i=input('user@atendente>>:')
    if i == '1':
        nome=input('digite o nome do paciênte:')
        if not validar_nome(nome):
            continue
        qtd, primeiro_atend, prox_atend = add_paciente(nome,qtd, primeiro_atend, prox_atend)
    elif i == '2':
        qtd, primeiro_atend, prox_atend = atender(qtd, primeiro_atend, prox_atend)
    elif i == '0':
        if qtd > 0:
            print('aplicação não pode ser encerrada')
        else:
            print('fim aplicação')
            break
    else:
        print('opção ínvalida')
        
