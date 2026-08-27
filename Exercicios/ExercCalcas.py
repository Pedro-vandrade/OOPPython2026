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
        print(f'Tecido : {self.tecido}')
        print(f'Estoque : {self.qtd_estoque} unidades')

    def aplica_desconto(self):
        desc = float(input('Digite a porcentagem do desconto: '))
        self.preco -= self.preco * (desc / 100)
        print(f'O valor atualizado é de: {self.preco}')


pants = Calca('Azul','G',285, 285, 'jeans')

pants.exibir_informacoes()
pants.aplica_desconto()
