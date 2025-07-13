\# Student Management System



A simple, command-line student management system written in Python. This script demonstrates basic object-oriented programming principles, including class creation, object instantiation, and list manipulation.



This project was created as a Python version of a Java school assignment.



\## Features



\-   **Student Class**: Represents a student with a name, ID, email, and grade.

\-   **StudentManager Class**: Manages a collection of `Student` objects.

\-   **Operations**:

&nbsp;   -   Add students to the list.

&nbsp;   -   Remove students from the list.

&nbsp;   -   Sort students by grade in descending order.

&nbsp;   -   Display the list of students at various stages.



\## How to Run



This script is self-contained and requires no external libraries. You can run it directly from your terminal.



1\.  Make sure you have Python 3 installed.

2\.  Save the code as a Python file (e.g., `student\_manager.py`).

3\.  Navigate to the directory where you saved the file and run the following command:



```bash

python student\_manager.py



Expected Output

The script will run without any user input and produce the following output, demonstrating the functionality of the system:



ArrayList before adding students:

The list is empty.



ArrayList after adding students:

Student(name='Amin Zamani', id=1, email='zama0039@algonquinlive.com', grade=3.9)

Student(name='John Kramer', id=2, email='Kram@gmail.com', grade=3.4)

Student(name='Hans Zimmer', id=3, email='Hans@yahoo.com', grade=3.5)

Student(name='Hannibal Lecter', id=4, email='HLecter@hotmail.com', grade=3.4)



ArrayList after sorting:

Student(name='Amin Zamani', id=1, email='zama0039@algonquinlive.com', grade=3.9)

Student(name='Hans Zimmer', id=3, email='Hans@yahoo.com', grade=3.5)

Student(name='John Kramer', id=2, email='Kram@gmail.com', grade=3.4)

Student(name='Hannibal Lecter', id=4, email='HLecter@hotmail.com', grade=3.4)



ArrayList after removing student Hans Zimmer:

Student(name='Amin Zamani', id=1, email='zama0039@algonquinlive.com', grade=3.9)

Student(name='John Kramer', id=2, email='Kram@gmail.com', grade=3.4)

Student(name='Hannibal Lecter', id=4, email='HLecter@hotmail.com', grade=3.4)



