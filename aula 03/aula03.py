# classes em python

# nome classe

# definição da classe
class Conta:
# definição dos atributos
    numero = 0
    saldo = 0.0

# cria uma variavel para chamar a função e alterar a variavel que iniciou com atributo vazio ou emm zero
pedro_conta=Conta()
pedro_conta.numero=2615
pedro_conta.saldo = 4500.00

vica_conta = Conta()
vica_conta.numero = 5120
vica_conta.saldo = 5000.00

pedro_conta.saldo -= 250
vica_conta.saldo += 250

lucy_conta = Conta()
lucy_conta.numero = 1000
lucy_conta.saldo = 1094

print(f'Conta do Pedro : {pedro_conta.saldo}')
print(f'Conta da Vica : {vica_conta.saldo}')

vica_conta.saldo -= 100
pedro_conta.saldo -= 100
lucy_conta.saldo += 200

print(f'Conta do Pedro : {pedro_conta.saldo}')
print(f'Conta da Vica : {vica_conta.saldo}')
print(f'Conta da Lucy : {lucy_conta.saldo}')
