
class Owner:

    def __init__(self, name: str, cpf: str, email: str, phone: str):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone = phone

    def owner_info(self):
        print(f'Name: {self.name} | CPF: {self.cpf} | Email: {self.email} | Phone: {self.phone}')

class Agent:
    def __init__(self: str, name: str, creci: str):
        self.name = name
        self.creci = creci

    def sell_property(self):
        res = input("Do you wanna sell the property ? [S/N]").strip().upper()
        if res == "S":
            self




class Property:
    def __init__(self, id: int, address: str, type: str, price: float, status: str, owner: Owner, agent: object) -> object:
        self.id = id
        self.address = address
        self.type = type
        self.price = price
        self.status = status
        self.owner = owner
        self.agent = agent

    def change_status(self):
        self.status = str("Digite o status do imovel (Disponível - Alugado - Vendido): ")
        self.status.lower()


owner1 = Owner('pedro', '0323', 'pedro@email.com', '51 9413')
agent1 = Agent('Haroldo', '1234')
owner1.owner_info()

prop = Property(0o1, 'Street 123', 'house', 250000, 'disponivel', owner1, agent1)
