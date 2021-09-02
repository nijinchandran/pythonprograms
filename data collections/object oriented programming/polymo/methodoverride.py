class Books:
    def printval(self,name):
        self.name=name
        print("physics",self.name)

class Child(Books):
    def printval(self,class1):
        self.class1=class1
        print("12",self.class1)

ch=Child()
ch.printval("physics")

#child class method overrides parent class method