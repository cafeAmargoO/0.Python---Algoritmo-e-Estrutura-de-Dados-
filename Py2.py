# fila de hospital utilizando fila circular

fila_pacientes = [None] * 10
qtd = 0
prox_paciente = 0
ult_paciente = 0

def inserir_paciente(paciente,qtd,prox_paciente,ult_paciente):
    if (qtd == len(fila_pacientes)):
        print('fila cheia')
    else:
        # se tiver [1] paciente
        if qtd != 0:
            # e a quantidade de ultimos pacientes chegar ao final
            ult_paciente = (ult_paciente +1) % len(fila_pacientes)

        # enquanto não chegar ao final
        fila_pacientes[ult_paciente] = paciente # adicione o paciente ao proximo a ser atendido
        # add paciente
        qtd = qtd + 1
        print('paciente inserido na fila')

        # senão, acrescenta o primeiro valor em [prox_paciente]
    return qtd, prox_paciente, ult_paciente

def remover_paciente(qtd,prox_paciente,ult_paciente):
    if (qtd == 0):
        print('fila vazia')
    else:
        # remove o primeiro paciente
        fila_pacientes[prox_paciente] = None
        prox_paciente = (prox_paciente +1) % len(fila_pacientes) # se a listagem chegar ao final
        qtd = qtd - 1
        # reseta
        if qtd == 0:
            prox_paciente = ult_paciente = 0

    return qtd, prox_paciente, ult_paciente

while True:
    print('[0] - sair')
    print('[1] - inserir paciênte')
    print('[2] - atender paciênte')
    print('[3] - visualisar paciêntes')

    user = input('opção:')
    
    if user == '1':
        nome = input('nome do paciênte:')
        qtd,prox_paciente,ult_paciente = inserir_paciente(nome,qtd,prox_paciente,ult_paciente)
    elif user == '2':
        qtd,prox_paciente,ult_paciente = remover_paciente(qtd,prox_paciente,ult_paciente)
    elif user == '3':
        print(fila_pacientes)
        print('atender:',prox_paciente)
        print('próximos da fila:',ult_paciente)
    elif user == '0':
        print('sistema desligado')
        print(fila_pacientes)
        break
    else:
        print('opção ínvalida')
    
