class Name:
    def __init__(self, FirstName, LastName, MiddleName):
        self.FirstName = FirstName
        self.LastName = LastName
        self.MiddleName = MiddleName

class Student_Details:
    def __init__(self, RollNo, StudentName, CourseName):
        self.RollNo = RollNo
        self.StudentName = StudentName
        self.CourseName = CourseName

Student_Details_1 = Student_Details(90, Name("vysh", "pooj", "moun"), "python")
Student_Details_2 = Student_Details(30, Name("vyshu", "pooji", "mouni"), "pythoni")

students = [Student_Details_1, Student_Details_2]

for std in students:
    print("RollNo: {}\n StudentName: {} {} {} \n CourseName: \n{}".format(std.RollNo, std.StudentName.FirstName, std.StudentName.MiddleName, std.StudentName.LastName, std.CourseName))
