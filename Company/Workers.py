
class Employee:

    def __init__(self, name, salary, sector, idnumber):
        self.name = name
        self.salary = salary
        self.sector = sector
        self.idnumber = idnumber

    def __str__(self):
        return f"ID: {self.idnumber} | Name: {self.name} | Salary: {self.salary} | Sector: {self.sector}"


def registry():
    print("---- Employee's Registry ----")
    name = str(input("inform the employee's name: "))
    salary = float(input("Inform the employee's salary: "))
    sector = str(input("Inform the employee's sector: "))
    idnumber = int(input("Inform the employee's id number: "))

    return Employee(name, salary, sector, idnumber)


employes = []

emp1 = registry()
print(emp1)

for _ in range(3):
    empl = registry()
    employes.append(empl)

print("Lista de Funcionarios")
for e in employes:
    print(e)