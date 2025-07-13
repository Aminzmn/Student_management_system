class Student:

    def __init__(self, name, id, email, grade):

        self.name = name
        self.id = id
        self.email = email
        self.grade = grade

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id}, email='{self.email}', grade={self.grade})"


class StudentManager:
    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, student):
        self._students.remove(student)

    def sortByGrade(self, grade):
        self._students.sort(key=lambda student: student.grade, reverse=True)

    def get_students(self):
        return self._students

def print_students(students):
    if not students:
        print("The list is empty")

    for student in students:
        print (student)

if __name__ == "__main__":
    top_students = StudentManager()

    print ("ArrayList before adding students:")
    print_students(top_students.get_students())

    student1 = Student("Amin Zamani", 1, "zama0039@algonquinlive.com", 3.9)
    student2 = Student("John Kramer", 2, "Kram@gmail.com", 3.4)
    student3 = Student("Hans Zimmer", 3, "Hans@yahoo.com", 3.5)
    student4 = Student("Hannibal Lecter", 4, "HLecter@hotmail.com", 3.4)

    top_students.add_student(student1)
    top_students.add_student(student2)
    top_students.add_student(student3)
    top_students.add_student(student4)


    print("\nArrayList after adding students:")
    print_students(top_students.get_students())

    top_students.sortByGrade(top_students.get_students())
    print("\nArrayList after sorting:")
    print_students(top_students.get_students())

    top_students.remove_student(student3)
    print("\nArrayList after removing student Hans Zimmer:")
    print_students(top_students.get_students())
