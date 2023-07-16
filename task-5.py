class Student :
    def __init__(self, age,):
        self.age = age
        self.grades = [ 5, 4, 3, 5 ,5]

    def add_grade(self, grade) :
        self.grades.append(grade)
    
    def get_average_grade(self) :
        return sum(self.grades)/ len(self.grades)
    
    def is_honors_student(self) :
        if self.get_average_grade() > 4.5:
            return True 
        else :
            return False


student = Student(10)
student.add_grade(5)
print(student.grades)
print(student.is_honors_student())