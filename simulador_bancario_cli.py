import sys

nome = input('Informe seu nome: ')
senha_digitada = ''
senha_correta = 203050
tentativas = 0
saldo = float(2000)
extrato = ''

while senha_digitada != senha_correta and tentativas < 3:
    senha_digitada = int(input('Informe a sua senha: '))
    if senha_digitada != senha_correta:
        tentativas += 1
        tentativas_restantes = 3 - tentativas
        if tentativas_restantes > 0:
            print(f'Senha incorreta você ainda tem {tentativas_restantes} tentativas')
if senha_digitada == senha_correta:
    print(f'Acesso Permitido! Bem-Vindo ao Pybank,{nome} .')
else:
    print('Acesso negado.')
    sys.exit()

opcao = 0

while opcao != 4:
    print('1 - Depósito')
    print('2 - Saque')
    print('3 - Extrato')
    print('4 - Sair ')
    opcao = int(input('Informe a opção desejada: '))

    if opcao == 1:
        deposito = float(input('Informe o valor do deposito: '))
        if deposito > 0:
            extrato += f'Depósito: {deposito:.2f} \n'
            saldo = saldo + deposito
            print(f'O valor de R${deposito:.2f} será depositado em sua conta')
            print(f'Valor total em conta: R${saldo:.2f}')
        else:
            print('Valor invalido!')
    elif opcao == 2:
        saque = float(input('Informe o valor que deseja sacar: '))
        if saque > 0 and saque <= saldo:
            extrato += f'Saque: {saque:.2f} \n'
            saldo = saldo - saque
            print(f'Saque autorizado valor restante na conta R${saldo:.2f} ')
        else:
            print('Saque Não Autorizado!')
    elif opcao == 3:
        if not extrato:
            print('Não foram realizadas movimentações')
        else:
         print('==========EXTRATO==========')
         print(extrato)
         print(f'Saldo Atual: R${saldo:.2f}')
         print('===========================')
    elif opcao == 4:
        print('Saindo do sistema...')
    else:
        print('opção invalida')



