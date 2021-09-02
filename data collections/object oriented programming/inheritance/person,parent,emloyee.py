class   Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)

class Parent:
    def setv(self,fname,fage):
        self.fname=fname
        self.fage=fage
        print(self.fname,self.fage)

class Employee(Person,Parent):
    def printv(self,salary,dprtmnt):
        self.salary=salary
        self.dprtmnt=dprtmnt
        print(self.salary,self.dprtmnt)

emp=Employee()
emp.set("anu",20,"abc")
emp.setv("dileep",54)
emp.printv(20000,"luminar")
