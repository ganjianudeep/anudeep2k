class Employee:
    #encapsulating name and salary attribute
    def __init__(self, name, salary):
        self.name = name
    # Here salary is a private attribute
        self.__salary = salary

#using get_salary & set_salary to access private attributes
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

# Inheritance
class Manager(Employee):
#Below method calls the constructor (__init__) of the parent class & passes the name and salary arguments
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)      #inheriting name, salary from parent class
        self.bonus = bonus

    # Polymorphism
    def get_salary(self):
        #get_salary method is over ridden in sub class for different implementation
        base_salary = super().get_salary()
        return base_salary + self.bonus

# Usage
employee = Employee("Robert", 1000)
print(f"{employee.name}'s salary: {employee.get_salary()}")

manager = Manager("Frost", 2000, 1000)
print(f"{manager.name}'s salary: {manager.get_salary()}")
