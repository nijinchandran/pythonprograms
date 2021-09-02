class Person:
    def __init__(self,name,age,adress):
        self.name= name
        self.age= age
        self.adress= adress

    def printval(self):
        print(self.name,self.age,self.adress)
obj=Person("anu",26,"abc")
obj.printval()