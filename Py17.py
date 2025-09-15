''' Fila de atendimento de hospital utilizando método prioritário
    (Algoritmo)
    0 - insere/atende paciênte; x
    1 - verificar se a fila está cheia; x
    2 - verificar se a fila está vazia; x
    3 - verificar o paciênte prioritário e atender primeiro; x

    (Regras do Algoritmo)

    0 - verificar se o nome é um nome válido; x 
    1 - verificar a idade, se a idade for menor que 18, 
    encaminhar para pediatria; x
    
'''

fila = [None] * 12
qtd = 0

def validar_nome(nome):
    if not nome or nome.strip() == '': # se nome for [None] ou vazio;
        print('erro: o espao não pode está vazio')
        return False
    if nome.isdigit(): # se tiver número;
        print('erro: nome não pode ser númerico')
        return False

    return True

def inserir_paciente(paciente,qtd):
    if qtd == len(fila):
        print('fila cheia')
    else:
        fila[qtd] = paciente
        qtd = qtd + 1
        print('paciênte inserido')
        
        if paciente[1] < 18:
            print(f'paciênte {paciente[0]} com idade {paciente[1]} será encaminhado para pediatria')
            
    return qtd

def atender(qtd):
    pessoa = None
    if qtd == 0:
        print('fila vazia')
    else:
        prio = False
        for i in range(qtd):
            if fila[i][1] >= 65:
                prio = True
                ind_prio = i
                break

        if prio == True:
            pessoa = fila[ind_prio] # remover
            for i in range(ind_prio,qtd-1): # do item removido atéo final[-1] 
                fila[i] = fila[i + 1] # desloca os elementos para a esuqerda da fila

            fila[qtd -1] = None   # evita duplicidade na lista
            qtd = qtd -1
            print('paciênte prioritário atendido')
        else:
            pessoa = fila[0]
            for i in range(qtd-1):
                fila[i] = fila[i + 1]

            fila[qtd-1] = None
            qtd = qtd - 1
            print('paciênte atendido')
            
    return pessoa, qtd

def visualizar():
    print('fila de atendimento')
    for i, paciente in enumerate(fila):
        if paciente is not None:
            texto = f"{i + 1}. {paciente[0]} - anos {paciente[1]}"
            if paciente[1] >= 65:
                texto += "(PRIORITARIO) "
            elif paciente[1] < 18:
                texto += " (PEDIATRIA) "
            print(texto)
        
while True:
    print('Fila de atendimento')
    print('[0] - sair')
    print('[1] - inserir paciênte')
    print('[2] - atender paciênte')
    print('[3] - visualizar fila')
    print('próximo a ser atendido:',fila[0])
    usuario = input('usuario@usuario>>:')
    if usuario == '1':
        
        nome = str(input('nome do paciênte>>:')).strip()
        if not validar_nome(nome): '''enquanto nome não retornar True, ignore o restante do código [continue]'''
            continue
        try:
           idade = int(input('idade>>:')) # verifico o tipo de valor ao digitar a idade
           if idade <= 0:
               print('erro: o número deve ser positivo')
               continue
            
           paciente = (nome,idade)
           qtd = inserir_paciente(paciente,qtd)
        except ValueError:
            print('erro: o valor deve ser inteiro')
    elif usuario == '2':
        pessoa, qtd = atender(qtd)
    elif usuario == '3':
        visualizar()
    elif usuario == '0':
        if qtd > 0:
            print('Não é possível encerrar o sistema')
            continue
        else:
            print('fim aplicação')
            break
    else:
        print('opção ínvalida')
