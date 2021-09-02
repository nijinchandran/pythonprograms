 class Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)

class Child(Person):
    def setv(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)

class Parent(Person):
    def setv(self,fname,fage):
        self.fname=fname
        self.fage=fage
        print(self.fname,self.fage)

class Student(Child):
    def printv(self,rollno,mark):
     self.rollno=rollno
     self.mark=mark
     print(self.rollno,self.mark)


st=Student()
st.set("anu",23,"abc")
st.setv("luminar",12)
st.setv("ram",56)
st.printv(2,78)