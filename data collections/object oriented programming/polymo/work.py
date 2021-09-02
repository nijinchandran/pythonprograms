class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno-rollno
        self.course=course
        self.mark=mark


    def printvalue(self):
        print("name::",self.name)
        print("rollno::",self.rollno)
        print("course::",self.course)
        print("mrk::",self.mark)

    def __str__(self):
        return self.name

f=open("student1",'r')
for line in f:
    data=line.split(",")
    name=data[0]g
    rollno=data[1]
    course=data[2]
    mark=data[3]
    obj=Student(name,rollno,course,mark)
    print(obj)
    obj.printvalue()