class Teacher:
    college_name='Luminar'
    def __init__(self,name,subject,department,id):
        self.name=name
        self.subject=subject
        self.department=department
        self.id=id

    def printval(self):
        print(self.name)
        print(self.subject)
        print(self.department)
        print(self.id)
        print(Teacher.college_name)

te=Teacher("anu","maths","science",1)
te.printval()