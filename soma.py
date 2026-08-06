# função sem parametros com retorono de valore



def soma(n1,n2):
    return (n1+n2)

def subtrai(n1,n2):
    return (n1 - n2)

def multi(n1,n2):
    return (n1 * n2)

def divisao(n1,n2):
    return (n1 / n2)

operacoes = ['+', '-','*','/']
continua ="S"

while True: # repetição Principal do Programa
    if continua != 'S':
        break
    while True: # try controle de erro
        try:

            op='k'
            n1=float(input('Digite um número:'))
            while op not in operacoes:
                op = input('Digite uma operação ( + - * / ):')
                if op not in operacoes:
                    print('Digite uma operação valida')
            n2 = float(input('Digite um número:'))
            break
        except:
            print('Digite somente FLOATS')

    if op == '+':
        print(f'Soma {n1} + {n2} = {soma(n1,n2)}')
    elif op == '-':
        print(f'Subtração {n1} - {n2} = {subtrai(n1,n2)}')
    elif op == '*':
        print(f'Multiplicação {n1} * {n2} = {multi(n1,n2)}')
    elif op == '/':

        continua=input('Continua (S/N):').upper()
        print('Tchau!')


soma()
multi()
divisao()
subtrai()