

class Calca:

    def __init__(self, cor, tamanho, preco, qtd_estoque, tecido):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.qtd_estoque = qtd_estoque
        self.tecido = tecido

    def exibir_informacoes(self):
        print(f'Cor : {self.cor}')
        print(f'Tamanho : {self.tamanho}')
        print(f'Preço : {self.preco}')
        print(f'tipo Gola : {self.tipo_gola}')
        print(f'Estoque : {self.qtd_estoque} unidades')


