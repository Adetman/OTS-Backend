#Student Result Checker
print('*** STUDENT RESULT CHECKER ***')

#Get Student Information
student_name = input("Enter student's name: ")
subject = input("Enter subject: ")

#Get Student Score
score = float(input("Enter student score: "))

#Check Student Result
if score >= 90 and score <= 100:
    grade = "A+"
    status = "PASSED"
    print("Congratulations,", student_name, "you have", status, subject, "with grade", grade)

elif score >= 75 and score <= 89:
    grade = "A"
    status = "PASSED"
    print("Congratulations,", student_name, "you have", status, subject, "with grade", grade)

elif score >= 60 and score <= 74:
    grade = "B"
    status = "PASSED"
    print("Congratulations,", student_name, "you have", status, subject, "with grade", grade)

elif score >= 50 and score <= 59:
    grade = "C"
    status = "PASSED"
    print("Congratulations,", student_name, "you have", status, subject, "with grade", grade)

elif score >= 40 and score <= 49:
    grade = "D"
    status = "PASSED"
    print("Congratulations,", student_name, "you have", status, subject, "with grade", grade)

elif score >= 0 and score <= 39:
    grade = "F"
    status = "FAILED"
    print("Sorry,", student_name, "you have", status, subject, "with grade", grade)

else:
    print("Invalid score! Please enter a score between 0 and 100.")