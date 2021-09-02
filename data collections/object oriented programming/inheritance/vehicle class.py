class Vehicle:
    def __init__(self,model,colour,regno):
        self.model=model
        self.colour=colour
        self.regno=regno


    def printval(self):
        print(self.model,self.colour,self.regno)


ve=Vehicle("KTM","KL12AE3456","Black")
ve.printval()
