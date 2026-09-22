# Restaurante
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.pedidos = [] # lista para adicionar pedidos

    def add_order(self, pedido):
        self.pedidos.append(pedido)
        # Estabelecendo associação direcional
        if pedido.cliente != self:
            pedido.cliente = self

    

