class Student:
    college="ABC"
    def __init__(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep
    def printv(self):
        print(self.name,self.rollno,self.dep,Student.college)
    def __str__(self):
        return self.name+str(self.rollno)


st=Student("anu",2,"cs")
st.printv()