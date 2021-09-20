class Employee:
    def __init__(self,name,age,salary,designation=None):    
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation
    def increment(self, incrment=0,desig=''):
        self.salary = self.salary+incrment
        print("The salary + increment is",self.salary,'of designations',desig)
class Internee(Employee):
    def __init__(self, name, age, salary=0):
        super().__init__(name, age, salary)
class JuniorDev(Employee):
    def __init__(self, name, age, salary=20000):
        super().__init__(name, age, salary)
name = input("Enter your name: ")
age = input("Enter your age: ")
salary = int(input("If you are a internee, Enter your desire value: "))
object1 = Internee(name,age)
print(object1.increment(salary,'Junior.Dev'))