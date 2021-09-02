class Employee:
    company='luminar'
    def setval(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(Employee.company)

em1=Employee()
em1.setval("amal",18,20000)
em1.printval()