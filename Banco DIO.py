import textwrap

def menu():
    menu = """\n

    [d]. Depositar 
    [s]. Sacar
    [e]. Extrato
    [c]. Nova conta 
    [l]. Lista contas 
    [u]. Novo usuário
    [x]. Sair 
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('\n--- Depósito realizado com sucesso! ---')
        print(f'\n--- Saldo atualizado: R$ {saldo:.2f} ---')
    else:
        print('\n### Operação falhou, o valor informado é inválido ###')

    return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite, n_saques, l_saques):
    ex_saldo = valor > saldo
    ex_limite = valor > limite
    ex_saques = n_saques >= l_saques

    if ex_saldo:
        print('\n### Operação falhou. Você não tem saldo suficiente ###')
        print(f'\n--- Seu saldo atual é: R$ {saldo:.2f} ---')
    elif ex_limite:
        print('\n### Operação falhou. Número máximo de saques excedido ###')

    elif ex_saques:
        print('\n### Operação falhou. Numero máximo de saques excedido ###')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'    
        n_saques += 1
        print('\n--- Saque realizado com sucesso ---')
        print(f'\n--- Seu saldo atual é: R$ {saldo:.2f} ---')

    else:
        print('\n### Operação falhou. O valor informado é inválido ###')
        

    return saldo, extrato 

def exibir_extrato(saldo, /, *, extrato):
    print('\n------------- EXTRATO -------------')
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'Saldo R$ {saldo:.2f}\n')

def c_usuario(usuarios):
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n### Já existe usuário com esse CPF ###')
        return
    nome = input('Informe o nome completo ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('--- Usuário criado ---')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def c_conta(agencia, n_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n- Conta criada com sucesso -')    
        return {'agencia': agencia, 'n_conta': n_conta, 'usuario': usuario}

def l_conta(conta):
    for conta in conta:
        linha = f'''\
            Agência: {conta['agencia']}
            C/C {conta['n_conta']}
            Titular: {conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    L_SAQUES = 3 
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    n_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                n_saques=n_saques,
                l_saques=L_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'u':
            c_usuario(usuarios)

        elif opcao == 'c':
            n_conta = len(contas) + 1
            conta = c_conta(AGENCIA, n_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'l':
                l_conta(contas)

        elif opcao == 'x':
                print('Saindo...')
                break

        else:
                print('OpeOperação inválida, por favor selecione novamente a operação desejada')

main()