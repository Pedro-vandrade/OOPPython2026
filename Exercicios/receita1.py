# Gelato de manga com maracujá
# 150 g de manga picada e congelada.
# ½ maracujá azedo (polpa).
# 2 colheres (sopa) de iogurte natural.
# Aproximadamente 10 minutos.


class Receita ():

    def __init__(self,nome: str = "Gelato de manga com maracujá",
        tempo_prep: int = 10, manga_g: float = 150.0,
        maracuja_un: float = 0.5,
        iogurte_colheres: float = 2.0,
        rendimento: int = 1
    ):
        self.nome = nome
        self.tempo_prep = tempo_prep
        self.manga_g = manga_g
        self.maracuja_un = maracuja_un
        self.iogurte_colheres = iogurte_colheres
        self.rendimento = rendimento

    def receitabase(self):
        print(f'A receita base é composta por {self.manga_g}g de manga picada congelada.\n'
              f'{self.maracuja_un} macarcujá azedo (polpa).\n'
              f'{self.iogurte_colheres} colheres de sopa de iogurte natural.\n'
              f'Que rendem {self.rendimento} porção individual, que levam {self.tempo_prep} min de preparo.')

    def calc_porcao(self):
        nova_porcao = int(input("Digite quantas porções você irá fazer: "))
        self.tempo_prep *= nova_porcao
        self.manga_g *= nova_porcao
        self.maracuja_un *= nova_porcao
        self.iogurte_colheres *= nova_porcao
        self.rendimento *= nova_porcao

        print(f'Para {nova_porcao} porções serão necessários:\n'
              f'{self.manga_g} g de manga.\n'
              f'{self.maracuja_un} unidades de maracujá.\n'
              f'{self.iogurte_colheres} colheres de sopa de iogurte.\n'
              f'Com tempo de preparo de {self.tempo_prep} minutos.'
              )


gelato = Receita()
gelato.receitabase()
gelato.calc_porcao()
