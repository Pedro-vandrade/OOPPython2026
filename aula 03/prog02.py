# definição de classe - criamos a classe
class Conta():

    # definimos o metodo e chamamos ele
    # definição de metodo
    def abertura(self, numconta, saldo):
        self.numconta = numconta
        self.saldo = saldo
        print(f'Conta aberta com sucesso! Seu saldo é de {self.saldo} e seu número de conta é {self.numconta}')

    def listar(self):
        print('\n********************')
        print(f'Número {self.numconta}')
        print(f'Saldo {self.saldo}')

# inicio do programa
# criando as intancias do objeto

vica_cc = Conta()
pedro_cc = Conta()
haroldo_cc = Conta()

# chamando o metodo e abrindo a conta do user
vica_cc.abertura(5412,6000.00)
vica_cc.listar()