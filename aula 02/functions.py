def hello():
    print('Hello World!')


# for i in range(10):
#     hello()
# print('Fim do programa')

def hello(nome):
    print(f' Olá, {nome}')
    print(f'Bem vindo {nome}')
    if nome == 'Gabriel':
        print('eai man')

while True:
    nomealuno = input('Digite um nome:').upper()
    if nomealuno =='fim':
        break
    hello(nomealuno)
    print('fim do programa')