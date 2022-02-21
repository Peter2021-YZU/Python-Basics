# Create a  class and initialize it
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print(self):
        print("Hi, I am " + self.name, " I am ", self.age, " and I am currently earning ", self.salary, " dollars a year")


# create an object of my class
Emp1 = Employee("Peter", 45, 100000)
#print the properties of my object
Emp1.print()


# Modify on my objects properties
Emp1.salary = 110000
Emp1.print()
