menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Quit

=>'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':  #DEPÓSITO
        print('Depósito\n')

        valor = float(input('Valor do depósito R$: '))

        if valor > 0:
            saldo += valor
            extrato += f'Você depositou o valor de R$ {valor:.2f}\n'
        else:
            print('Valor não permitido')

    elif opcao == 's':  #SAQUE
        print('Saque\n')

        valor = float(input('Qual valor você deseja sacar R$: '))

        excedeu_saldo = valor > saldo
        excedeu_limit = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou, Você excedeu o saldo')

        elif excedeu_limit:
            print('Operação falhou, Você excedeu o limite')

        elif excedeu_saque:
            print('Operação falhou, Você excedeu os saques diários')

        elif valor > 0:
            saldo -= valor
            extrato += f'Você fez um saque de R$ {valor:.2f}\n'
            numero_saques += 1
        

    elif opcao == 'e': ## EXTRATO
        print('\n====================EXTRATO====================')
        print('\nNão foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo do usuário é de R$ {saldo:.2f}')
        print('\n====================EXTRATO====================')



    elif opcao == 'q':  #QUIT
        break
    else:
        print('Operação inválida, selecione a operação desejada!')