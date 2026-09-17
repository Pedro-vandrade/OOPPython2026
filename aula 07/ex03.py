#Televisão
class TV:

    def __init__(self,TVmodel):
        self.TVmodel= TVmodel
        self.volume = None
        self.chanel = None
        self.state = 'desligada'

    def ligar(self):
        self.chanel = 0
        self.volume = 0
        self.state = 'ligada'
        print('TV Ligada')


    def desligar(self):
        self.state = 'desligada'
        print('TV Desligada')

    def aumentarvolume(self):
        if self.state != 'ligada':
            print("Tv desligada.")
            return

        volume_inserido = int(input("Digite o volume: "))

        if self.volume >=1 or self.volume <= 100:
            self.volume += volume_inserido
            print(f'Volume atual: {volume_inserido}')

    def diminuirvolume(self):
        if self.state != 'ligada':
            print('TV Desligada.')
            return

        volume_inserido = int(input("Digite o volume: "))
        if self.volume >= 1 or self.volume <= 100:
            self.volume -= volume_inserido
            print(f'Volume atual: {volume_inserido}')

tvsala = TV('LG')
tvsala.ligar()
tvsala.aumentarvolume()
tvsala.diminuirvolume()
