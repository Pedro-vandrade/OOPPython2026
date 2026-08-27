
class Vehicle():
    #self defibne os atributos do objeto
    def __init__(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.velocidade = 0

    def list_details(self):
        print(f'Marca : {self.marca}')
        print(f'Modelo : {self.modelo}')
        print(f'Ano : {self.ano}')
        print(f'Motor : {self.motor}')
        print(f'Velocidade : {self.velocidade} km/h')

    def accelerate(self):
        acelera = int(input("Digite a velocidade: "))
        self.velocidade += acelera
        print(f'A velocidade atual é de : {self.velocidade} km/h')

    def brake(self):
        freia = int(input("Digite a o quanto quer diminuir a velocidade: "))
        self.velocidade -= freia
        print(f'A velocidade atual é de : {self.velocidade} km/h')

    def changeengine(self):
        print(f'O motor atual do seu {self.modelo} é um {self.motor}.')
        self.motor = str(input("Digite o motor a ser instalado: "))
        print(f'Seu {self.modelo} agora possui um motor {self.motor}.')




car = Vehicle('GM', 'Onix', 2022, '1.6')

car.list_details()
car.accelerate()
car.brake()
car.changeengine()