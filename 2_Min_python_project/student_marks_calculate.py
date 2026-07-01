Student_name = input("Please Enter Student Name: ")

sub1 = int(input("Marks in Telugu: "))
sub2 = int(input("Marks in Hindi: "))
sub3 = int(input("Marks in English: "))
sub4 = int(input("Marks in Maths: "))
sub5 = int(input("Marks in Science: "))
sub6 = int(input("Marks in Social: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
avg_marks = total_marks / 6
percentage = (total_marks / 600) * 100

grade = ""
if percentage > 90:
    grade = " A "
elif percentage >= 80 and percentage <= 90:
    grade = " B "
elif percentage >= 70 and percentage <= 80:
    grade = " c "
else:
    grade = " P "

print(f"Name: {Student_name},\nTotal_marks: {total_marks},\nAverage_Marks: {avg_marks}\nPercentage: {percentage}\nGrade: {grade}")