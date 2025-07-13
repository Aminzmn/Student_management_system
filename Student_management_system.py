class Student:
    """
    Represents a single student record, containing their details.
    """

    def __init__(self, name, student_id, email, grade):
        """
        Initializes a new Student object.

        Args:
            name (str): The full name of the student.
            student_id (int): The unique ID for the student.
            email (str): The student's email address.
            grade (float): The student's current grade.
        """
        self.name = name
        self.student_id = student_id
        self.email = email
        self.grade = grade

    def __repr__(self):
        """
        Provides an official, developer-friendly string representation of the object.
        This is useful for debugging and logging.
        """
        return f"Student(name='{self.name}', id={self.student_id}, email='{self.email}', grade={self.grade})"


class StudentManager:
    """
    Manages a collection of Student objects, providing methods to add,
    remove, and sort them.
    """
    def __init__(self):
        """
        Initializes the StudentManager with an empty list to hold students.
        """
        # The underscore prefix suggests this is an internal attribute.
        self._students = []

    def add_student(self, student):
        """
        Adds a single student object to the collection.

        Args:
            student (Student): The student instance to be added.
        """
        self._students.append(student)

    def remove_student(self, student):
        """
        Removes a specific student object from the collection.

        Args:
            student (Student): The student instance to be removed.
        """
        self._students.remove(student)

    def sort_by_grade(self):
        """
        Sorts the internal list of students by grade in descending order (highest first).
        """
        # The sort method is modified by a 'key' argument.
        # The lambda function tells sort() to use the 'grade' attribute of each
        # student as the value for comparison.
        # 'reverse=True' ensures the order is from highest to lowest.
        self._students.sort(key=lambda student: student.grade, reverse=True)

    def get_students(self):
        """
        Accessor method to retrieve the list of students.

        Returns:
            list: The current list of Student objects.
        """
        return self._students

def print_student_list(students):
    """
    A helper function to print each student in a list to the console.

    Args:
        students (list): A list of Student objects to be printed.
    """
    if not students:
        print("The list is empty.")
    else:
        for student in students:
            print(student)

# The __name__ == "__main__" block is standard Python practice.
# It ensures that the code inside this block only runs when the script is
# executed directly, not when it's imported as a module into another script.
if __name__ == "__main__":

    # --- Setup ---
    # Create an instance of the manager that will hold our student records.
    top_students = StudentManager()

    # --- Demonstrate Initial State ---
    print("ArrayList before adding students:")
    print_student_list(top_students.get_students())

    # --- Data Creation ---
    # Instantiate several Student objects to work with.
    student1 = Student("Amin Zamani", 1, "zama0039@algonquinlive.com", 3.9)
    student2 = Student("John Kramer", 2, "Kram@gmail.com", 3.4)
    student3 = Student("Hans Zimmer", 3, "Hans@yahoo.com", 3.5)
    student4 = Student("Hannibal Lecter", 4, "HLecter@hotmail.com", 3.4)

    # --- Add Operation ---
    # Add the newly created students to the manager's list.
    top_students.add_student(student1)
    top_students.add_student(student2)
    top_students.add_student(student3)
    top_students.add_student(student4)

    print("\nArrayList after adding students:")
    print_student_list(top_students.get_students())

    # --- Sort Operation ---
    # Call the sorting method to arrange students by grade.
    top_students.sort_by_grade()
    print("\nArrayList after sorting:")
    print_student_list(top_students.get_students())

    # --- Remove Operation ---
    # Demonstrate removing a specific student from the list.
    top_students.remove_student(student3)
    print("\nArrayList after removing student Hans Zimmer:")
    print_student_list(top_students.get_students())
