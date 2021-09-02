#single inheritance

class Person:                                #base class/parent class/super class
    def walk(self):
        print("person is walking")
    def read(self):
        print("person is reading")
class Student(Person):                      #derived class/sub class/child class
    def exam(self):
        print("student attending exam")

pe=Person()
pe.walk()
pe.read()

st=Student()
st.exam()
st.walk()
st.read()