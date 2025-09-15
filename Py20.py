''' Fila de máquina virtual de mercado baseado no arquivo
    Py17.py '''


fila = [None] * 8
qtd = 0
loop = True
# valido nome
def validar_nome(nome):
    if not nome or nome.strip() == '':
        print('erro: o espaço não pode tá vázio')
        return False
    if nome.isdigit():
        print('erro: nome não pode ter dígitos')
        return False

    return True
# insiro cliente
def inserir_cliente(cliente,qtd):
    if qtd == len(fila):
        print('fila cheia')
    else:
        fila[qtd] = cliente
        qtd = qtd + 1
        print('cliente inserido na fila')
    return qtd

def atender(qtd):
    sair = None
    if qtd == 0:
        print('fila vazia')
    else:
        # busca prio
        prio = False 
        for i in range(qtd):
            if fila[i][1] >= 65:
                prio = True
                ind_i = i
                break
        # caso ache, remove primeiro
        if prio == True:
            sair = fila[ind_i]
            for i in range(ind_i,qtd-1):
                fila[i] = fila[i + 1]

            fila[qtd-1] = None
            qtd = qtd - 1
            print('preferêncial atendido')

        else:
        # senão, executa fila circular 
            sair = fila[0]
            for i in range(qtd-1):
                fila[i] = fila[i + 1]

            fila[qtd-1] = None
            qtd = qtd - 1
            print('cliente atendido')
    return sair, qtd


while loop:
    print('[0] - sair')
    print('[1] - inserir cliente na fila')
    print('[2] - atender cliente')
    print(fila)
    user = input('user>>:')
    if user == '1':
        nome = str(input('nome do cliente>>:'))
        if not validar_nome(nome):
            continue

        try:
            idade = int(input('idade>>:'))
            if idade <= 0:
                print('erro: idade deve ser um número positivo')
            cliente = (nome,idade)
            qtd = inserir_cliente(cliente,qtd)
        except ValueError:
            print('erro: o número deve ser ínteiro')
            

    elif user == '2':
        sair, qtd = atender(qtd)
    elif user == '0':
        if qtd > 0:
            print('não é possível encerrar aplicação')
        else:
            print('fim aplicação')
            loop = False
    else:
        print('erro: opção ínvalida')
