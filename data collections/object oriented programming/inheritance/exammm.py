class Vehicle:
     def __init__(self,name,class):
         self.name=name
         self.class=class

    def printv(self):
         print(self.name)
         print(self.class)

class Child bus(Vehicle):

    def __init__(self, students,batch):
         super().__init__(name,class)
         self.students=students
         self.batch=batch


    def print(self):
        print(self.students)
        print(self.batch)


chl=Child bus(38,"10th","Luminar",10)
chl.printval()
chl.print()