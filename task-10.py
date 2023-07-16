class Employee :
    def __init__(self, position, salary) :
        self.position = position
        self.salary = salary

    def get_salary(self) :
        return self.salary
    
    def get_tax(self):
        return self.salary / 100 * 20
    
employee = Employee("director", 2500)
print(employee.get_salary())
print(employee.get_tax())