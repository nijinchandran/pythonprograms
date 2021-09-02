class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def printval(self):
        print("name",self.name)
        print("ae",self.age)


class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark

    def print(self):
        print(self.rollno)
        print(self.mark)
        print(self.name)
        print(self.age)



cr=Student(2,34,"anu",22)
cr.printval()
cr.print()