#Student class with name and score
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

#Grade to return true if passed
    def is_passed(self):
        return self.score >= 50

#Create an instance of the Student class
student1 = Student("Abel", 45)
student2 = Student("Betty", 75)

#Print whether the student passed
print(student1.is_passed())
print(student2.is_passed())
