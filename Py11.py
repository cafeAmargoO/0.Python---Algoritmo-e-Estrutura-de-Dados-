# fila prio de hospital

fila_pacientes = [None] * 8
pacientes = 0

def inserir_paciente(paciente,pacientes):
    if pacientes == len(fila_pacientes):
        print('fila cheia')
    else:
        fila_pacientes[pacientes] = paciente
        pacientes = pacientes + 1
        print('paciente inserido na fila')
        
    return pacientes

def atender(pacientes):
    pessoa = None
    if (pacientes == 0):
        print('fila vazia')
        
    else:
        vermelho = False
        for i in range(pacientes):
            if fila_pacientes[i][1] == 'VERMELHO'.upper():
                vermelho = True
                prio_paciente = i
                break

        if vermelho == True:
            pessoa = fila_pacientes[prio_paciente]
            for i in range(prio_paciente,pacientes-1):
                fila_pacientes[i] = fila_pacientes[i + 1]

            fila_pacientes[pacientes-1] = None
            pacientes = pacientes - 1
            print('paciente atendido')
            
        else:
            pessoa = fila_pacientes[0]
            for i in range(pacientes-1):
                fila_pacientes[i] = fila_pacientes[i + 1]

            fila_pacientes[pacientes-1] = None
            pacientes = pacientes - 1
            print('paciente atendido')

        return pessoa, pacientes
    
while True:
    print('[0] - sair')
    print('[1] - inserir paciente')
    print('[2] - atender paciente')
    print('[3] - visualizar fila')
    
    opt = input('escolha:')
    if opt == '1':
        
        nome = input('nome:')
        situacao = input('tipo de atendimento:').upper()
        paciente = (nome,situacao)
        pacientes = inserir_paciente(paciente,pacientes)
    elif opt == '2':
        pessoa, pacientes = atender(pacientes)
    elif opt == '3':
        print('fila atual:',fila_pacientes)        
    elif opt == '0':
        print('fila atual:',fila_pacientes)
        break    
    else:
        print('opção ínvalida')
    
                
        
