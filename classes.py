class Employee:
    def __init__(self, first, last, salary, email):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = email

    def fullname(self):
        return f"{self.first} {self.last}"
    
employee_1 = Employee("Sai", "Vanga", 150000, "sai@sai.programmer")
employee_2 = Employee("Sasidhar", "Vanga", 200000, "sasidhar@sasidhar.admin")

print(employee_1.first)
print(employee_1.last)
print(employee_1.email)

print(employee_2.first)
print(employee_2.last)
print(employee_2.email)

print(employee_1.fullname())
print(employee_2.fullname())