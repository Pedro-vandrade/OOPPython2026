fusca.marca = 'Volkswagen'
fusca.modelo= '2 portas'
fusca.ano=1970
fusca.motor='Gasolina 1300'
fusca.velocidade=0
fusca.listar()
print('acelerar')# 27/08/2026

class Veiculo:
    marca = ''
    modelo = ''
    ano = 0
    motor = ''
    velocidade=0

    def listar(self):
        print(f'\nMarca {self.marca}')
        print(f'Modelo {self.modelo}')
        print(f'Ano {self.ano}')
        print(f'Motorização {self.motor}')
        print(f'Velocidade {self.velocidade} Km/h {'em Movimento' if self.velocidade >0 else 'Parado' } ' )
    def acelerar(self):
        if self.velocidade >= 150:
            print(f'Alcançou Limite Máximo {self.velocidade}')
        else:
            self.velocidade+=10
    def frear(self):
        self.velocidade-=10
        if self.velocidade <= 0:
            self.velocidade =0


fusca = Veiculo()
for i in range(10):
    fusca.acelerar()
fusca.listar()
print('frear')
for i in range(12):
    fusca.frear()
fusca.listar()