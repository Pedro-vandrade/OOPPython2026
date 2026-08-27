class ReceitaBruschetta:

  def __init__(
      self,
      nome: str = 'Bruschetta de tomates assados e manjericão',
      tempo_prep: int = 30,
      pao_un: float = 1.0,
      tomate_un: float = 2.0,
      mucarela_g: float = 100.0,
      azeite_colheres: float = 1.0,
      rendimento: int = 2,
  ):
    self.nome = nome
    self.tempo_prep = tempo_prep
    self.pao_un = pao_un
    self.tomate_un = tomate_un
    self.mucarela_g = mucarela_g
    self.azeite_colheres = azeite_colheres
    self.rendimento = rendimento

  def receitabase(self) -> None:
    print(
        f'--- {self.nome} ---\n'
        f'A receita base é composta por:\n'
        f'• {self.pao_un:.0f} pão italiano ou baguete\n'
        f'• {self.tomate_un:.0f} tomates frescos\n'
        f'• {self.mucarela_g:.0f}g de queijo muçarela\n'
        f'• {self.azeite_colheres:.0f} colher de sopa de azeite de oliva extra virgem\n'
        f'• Folhas de manjericão, sal e pimenta-do-reino a gosto\n'
        f'Rendimento: {self.rendimento} porção(ões) | Tempo: {self.tempo_prep} min.\n'
    )

  def calc_porcao(self, nova_porcao: float) -> None:
      fator = nova_porcao / self.rendimento

      pao_total = self.pao_un * fator
      tomate_total = self.tomate_un * fator
      mucarela_total = self.mucarela_g * fator
      azeite_total = self.azeite_colheres * fator
      tempo_total = self.tempo_prep * fator  # Cálculo proporcional do tempo

      print(
          f'Para {nova_porcao} porção(ões) serão necessários:\n'
          f'• {pao_total:.1f} unidade(s) de pão italiano\n'
          f'• {tomate_total:.1f} unidade(s) de tomate\n'
          f'• {mucarela_total:.1f}g de muçarela\n'
          f'• {azeite_total:.1f} colher(es) de sopa de azeite\n'
          f'• Manjericão, sal e pimenta-do-reino a gosto\n'
          f'Tempo de preparo: {tempo_total:.0f} min.\n'
      )


# Execução
bruschetta = ReceitaBruschetta()
bruschetta.receitabase()

qtd = float(input('Digite quantas porções você deseja fazer: '))
bruschetta.calc_porcao(qtd)