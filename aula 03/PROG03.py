
# Você foi contratado para desenvolver a estrutura inicial de um sistema de cadastro. Para isso, você deve criar uma classe chamada Pessoa seguindo os passos abaixo:
#
# Definição da Classe e Atributos:
#
# nome (texto)
# idade (número inteiro)
# cpf (texto)
# email (texto)
# celular (texto)

# Criação dos Métodos:
# cadatrar(self,nome,idade,cpf,email,celular): Método que atribui os valors ao objeto conforme  os 5 dados passados como parâmetros para a pessoa de forma organizada.
#
# exibir_dados(self): Método que imprime na tela todos os 5 dados cadastrados da pessoa de forma organizada.
#
# alterar_celular(self, novo_celular): Método que recebe um novo número de telefone como parâmetro e atualiza o atributo celular do objeto.
#
# Código Principal (Teste prático):

# Crie (instancie) um objeto da classe Pessoa com dados fictícios.
# Chame o método exibir_dados() para mostrar as informações iniciais.
# Chame o método alterar_celular(...) passando um novo número.
# Chame novamente o método exibir_dados() para confirmar se o número do celular foi realmente atualizado.


class Pessoa():
    nome: ''
    idade = 0
    cpf = ''
    email = ''
    celular = ''

    def cadastro(self, nome, idade, cpf,email, celular):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.celular = celular


    def exibir_dados(self):
        print(f'Nome : {self.nome}')
        print(f'Idade : {self.idade}')
        print(f'CPF : {self.cpf}')
        print(f'email : {self.email}')
        print(f'Celular : {self.celular}')

    def altera_cel(self,novo_celular):
        self.celular = novo_celular
        print(f'o novo celuar de {self.nome} é {self.celular}')

nome_input = input('Digite o nome: ')
idade_input = input('Digite a idade: ')
cpf_input = input('Digite o cpf: ')
email_input = input('Digite o email: ')
celular_input = input('Digite o celular: ')


pedro_cad = Pessoa()
pedro_cad.cadastro(nome_input,idade_input,cpf_input,email_input,celular_input)
pedro_cad.exibir_dados()

novo_celular_input = input('Digite o novo celular: ')
pedro_cad.altera_cel(novo_celular_input)
pedro_cad.exibir_dados()
