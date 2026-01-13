class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def get_name(self):
        return self.name

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        return sum([student.get_grade() for student in self.students]) / len(
            self.students
        )

    def get_student_names(self):
        return [student.get_name() for student in self.students] 

    def get_student_grades(self):
        return [student.get_grade() for student in self.students]


def main():
    s1 = Student("Emmy", 20, 95)
    s2 = Student("Dammy", 25, 90)
    s3 = Student("Kwaku", 28, 88)

    course = Course("Math", 2)
    course.add_student(s1)
    course.add_student(s2)
    print(course.get_average_grade())
    print(course.get_student_names())
    print(course.get_student_grades())


main()
