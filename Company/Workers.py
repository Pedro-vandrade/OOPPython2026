
class Employee:

    def __init__(self, name, salary, department, idnumber):
        self.name = name
        self.salary = salary
        self.department = department
        self.idnumber = idnumber

    def __str__(self):
        return f"ID: {self.idnumber} | Name: {self.name} | Salary: {self.salary} | Department: {self.department}"

    def give_raise(self,percentage):
        self.salary += self.salary * (percentage / 100)


def registry():
    print("---- Employee's Registry ----")
    name = str(input("inform the employee's name: "))
    salary = float(input("Inform the employee's salary: "))
    department = str(input("Inform the employee's department: "))
    idnumber = int(input("Inform the employee's id number: "))

    return Employee(name, salary, department, idnumber)




employes = []

emp1 = registry()
print(emp1)
print(f"Current Salary : {emp1.salary}")

taxraise = float(input("Inform the salary's raise percentage: "))
taxraise = round(taxraise, 1)
emp1.give_raise(taxraise)
print(f"Salary after raise: : {emp1.salary}")
print(emp1)

# for _ in range(3):
#     empl = registry()
#     employes.append(empl)
#
# print("Lista de Funcionarios")
# for e in employes:
#     print(e)