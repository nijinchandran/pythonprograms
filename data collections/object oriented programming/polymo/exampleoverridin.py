class Person:
    def printval(self,name):
        self.name=name
        print("name",self.name)

class Student(Person):
    def printval(self,school):
        self.school=school
        print("luminar",self.school)

st=Student()
st.printval("anu")