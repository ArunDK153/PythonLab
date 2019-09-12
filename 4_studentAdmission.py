class Student:
    def __init__(this):
        this.student_id = None
        this.marks = None
        this.age = None
    def getStudentId(self):
        return self.student_id
    def setStudentId(self,id):
        self.student_id = id
    def getMarks(self):
        return self.marks
    def setMarks(self,marks):
        self.marks = marks
    def getAge(self):
        return self.age
    def setAge(self,age):
        self.age = age
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age()):
            if self.marks>=65:
                return True
            else:
                return False
        else:
            return False

sList=[]
no = int(input("Enter number of students: "))
for i in range (no):
    sList.append(Student())
    print("Enter details for student")
    m = int(input("Enter marks: "))
    a = int(input("Enter age: "))
    sList[i].setStudentId(i+1)
    sList[i].setMarks(m)
    sList[i].setAge(a)
    if sList[i].check_qualification():
        print("Student ",i+1," is eligible for qualification.")
    else:
        print("Student ",i+1," is not eligible for qualification.")
