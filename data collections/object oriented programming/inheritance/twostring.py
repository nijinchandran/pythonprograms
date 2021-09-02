class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def printv(self):
        print(self.model,self.color,self.regno)
    def __str__(self):
        return self.model+self.color

ve=Vehicle("KTM","KL12AE3456","Black")
ve.printv()
print(ve)