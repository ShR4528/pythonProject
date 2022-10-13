class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first.lower()}.{last.lower()}@companyname.com'

    @property
    def email(self):
        return  f'{self.first.capitalize()} {self.last.capitalize()}'

    @property
    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'

    @fullname.setter
    def fullname(self):
        first,last = name.split()
        self.first


emp1 = Employee('Bob', 'Summers', 1000)
emp2 = Employee('Mary', 'Gold', 3000)

print(emp1.email)
print(emp1.fullname)
print(emp1.__dict__)
