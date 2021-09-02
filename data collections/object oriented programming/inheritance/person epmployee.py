class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def printval(self):
        print("name",self.name)
        print("ae",self.age)

class Employee(Person):
     def __init__(self,salary,cmpny,name,age):
        super().__init__(name, age)
        self.salary=salary
        self.cmpny=cmpny


     def print(self):
        print(self.salary)
        print(self.cmpny)




emp=Employee(20000,"luminar","anu",23)
emp.printval()
emp.print()