class Parent:
    def __init__(self,name,adrs):
        self.name=name
        self.adrs=adrs

    def printv(self):
        print(self.name,self.adrs)

class Teacher(Parent):

    def __init__(self,id,dprtmnt,name,adrs):
        super().__init__(name,adrs)
        self.id=id
        self.dprtmnt=dprtmnt

    def printval(self):
        print(self.id,self.dprtmnt,self.name,self.adrs)
    def __str__(self):
        return self.name+str(self.id)

re=Teacher(1,"cs","anu","abc")
print(re)
re.printval()

