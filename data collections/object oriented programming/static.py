class Student:
    school='luminar'
    def setval(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def printval(self):
        print(self.name)
        print(self.rollno)
        print(Student.school)

st1=Student()
st1.setval("amal",3)
st1.printval()