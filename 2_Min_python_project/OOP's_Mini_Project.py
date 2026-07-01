class student:

    def __init__(self , name , student_id):
        self.name = name
        self.student_id = student_id
        self.subject = {}                       #subject : Marks Dictionary

    def add_subject(self, subject , marks):
        self.subject[subject] = marks

    def total_marks(self):
        return sum(self.subject.values())
    
    def print_report_card(self):
        print("                   ", self.name ,"                     " )
        print("=================== Report Card ===============")
        print(f"Student Name :  {self.name}")
        print(f"Student id :    {self.student_id}")
        print("----------------------------------")

        for subject , marks in self.subject.items():
            print(f"{subject: <10} : {marks}")

        print("----------------------------------")
        print(f"Total_marks : {self.total_marks()}")
        print("----------------------------------")

# User Input

name = input("Please Enter Student Name: ")
student_id = int(input("Please Enter Student ID: "))

s1 = student(name, student_id)

for i in range(6):
    subject = input("Enter Subject Name: ")
    marks = int(input("Enter Marks: "))
    
    s1.add_subject(subject, marks)

s1.print_report_card()