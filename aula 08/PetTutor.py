class Tutor:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exb_dados_tutor(self):
        print('-' *15, 'TUTOR', '-'* 15)
        print(f'Tutor: {self.nome}')
        print(f'Telefone : {self.telefone}')
        print('-' *15, '-'* 15)

class Pet:
    def __init__(self, nome, especie, tutor):
        self.nome = nome
        self.especie = especie
        self.tutor = tutor

    def exb_dados_pet(self):
        print('-' *15, 'DADOS PET', '-'* 15)
        print(f'Nome: {self.nome}' )
        print(f'Especie: {self.especie} ')
        self.tutor.exb_dados_tutor()

tutor1 = Tutor('Pedro', '51 9413')
tutor1.exb_dados_tutor()

pet1 = Pet('Haroldo','Gato',tutor1)
pet1.exb_dados_pet()

