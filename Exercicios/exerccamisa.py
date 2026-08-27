# Objetivo: Praticar a criação de classes em Python, uso do construtor __init__, atributos de
# instância e métodos com validação condicional.
# Contexto:
# Você foi encarregado de desenvolver o módulo de controle de camisas para o sistema de uma
# loja de roupas. O sistema deve permitir o cadastro de novas peças, a visualização dos dados e
# o registro de vendas com baixa no estoque.
from symtable import Class

class Camiseta:

    def __init__(self, cor, tamanho, preco, tipo_gola, qtd_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.tipo_gola = tipo_gola
        self.qtd_estoque = qtd_estoque

    def details(self):
        print(f'Cor : {self.cor}')
        print(f'Tamanho : {self.tamanho}')
        print(f'Preço : {self.preco}')
        print(f'tipo Gola : {self.tipo_gola}')
        print(f'Estoque : {self.qtd_estoque} unidades')

    def vender(self):
        venda = int(input("Digite quantas peças foram vendidas: "))
        self.qtd_estoque -= venda
        if venda > self.qtd_estoque:
            print("Não possuimos essa quantidade.")
        elif venda > 0:
            print(f'Quantidades no estoque: {self.qtd_estoque}')
        elif venda <=0:
            print('Não é possivel vender unidades ou menos. ')








shirt = Camiseta('Azul', 'M', 89.90, 'Normal', 75)

shirt.details()
shirt.vender()
