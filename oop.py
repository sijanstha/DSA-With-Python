class Employee:

    # this is class variable
    raise_amount = 1.04

    # this is instance variable which is shared by all
    num_of_emps = 0

    # this is like constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):  # dont forget self instance
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # can be used as alternative constructor
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


class Developer(Employee):
    raise_amount = 1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            # print('inside none')
            self.employees = []
        else:
            # print('inside not none')
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emo(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev_1 = Developer('Sijan', 'Shrestha', 15000, 'Python')
dev_2 = Developer('Praveen', 'Nepali', 20000, 'Java')

mgr_1 = Manager('John', 'Cnea', 5000, [dev_1])
mgr_1.add_employee(dev_2)
print(mgr_1.email)
print(mgr_1.print_emps())
