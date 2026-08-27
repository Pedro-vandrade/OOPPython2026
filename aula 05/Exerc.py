
class Departamento():

    def __init__(self, codDepartamento, nomeDepartamento, nomeGerente,qtdFuncionarios):
        self.codDepartamento = codDepartamento
        self.nomeDepartamento = nomeDepartamento
        self.nomeGerente = nomeGerente
        self.qtdFuncionarios = qtdFuncionarios


    def listarDepartamento(self):
        print(f'Código: [{self.codDepartamento}] - Departamento: [{self.nomeDepartamento}] - Gerente: [{self.nomeGerente}] - Nº Funcionarios: [{self.qtdFuncionarios}]')

    def mudarGerente(self):
        self.nomeGerente = str(input('Digite o nome do novo gerente: '))
        self.listarDepartamento()

    def addDept(self):
        self.codDepartamento = int(input("Digite o código do departamento : "))
        self.nomeDepartamento = str(input('Digite o nome do departamento : '))
        self.nomeGerente = str(input('Digite o nome do gerente do departamento: '))
        self.qtdFuncionarios = int(input("Digite o numero de funcionarios : "))

        # self.listarDepartamento()


    def codInt(self):
        if self.codDepartamento is int:
            print('O Código do departamento é inteiro. ')
        else:
            print('Código do departamento não é um numero inteiro')


dept = Departamento(12, 'TI', 'João', 0)

dept.listarDepartamento()
dept.mudarGerente()
dept.codInt()
dept.addDept()
dept.listarDepartamento()


# new_manager = input('Digite o nome do novo gerente:')
# dept.mudarGerente(new_manager)