class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self,raiseamt=5000):
        self.annual_salary = self.annual_salary + raiseamt
        return self.annual_salary

sam = Employee('sam','chia',5000)
print(sam.give_raise())