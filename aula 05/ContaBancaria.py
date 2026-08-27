from time import sleep


class ContaBancaria():

    def __init__(self, numconta, titular, saldo):
        self.numconta = numconta
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        deposito = float(input("Digite o valor a ser depositado: "))
        self.saldo =+ deposito
        if deposito <= 0:
            print('Digite um valor maior que zero.')

    def exibirConta(self):
        print(f'Nº Conta: [{self.numconta}] - Titular: [{self.titular}] - Saldo: [{self.saldo}]')

    def saque(self):
        saque = float(input('Digite o valor do saque: '))
        self.saldo -= saque
        if self.saldo < saque:
            print(f'Valor indisponivel para saque. Saldo atual é de {self.saldo}.')
        else :
            print(f'Saldo atualizado: {self.saldo}')


num = int(input('Digite o numero da conta : '))
nome = input('Titular da conta: ')

contabanco = ContaBancaria(num, nome, 0)
contabanco.depositar()
contabanco.exibirConta()
contabanco.saque()
