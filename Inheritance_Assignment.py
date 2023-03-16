
# Here, I create a parent class, Person
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


# I am going to create two child classes. The first one would be Student.

class Student(Person)
    def __init__(self, fname, lname, age, grade):
        super().__init__(fname, lname)  # super() allows Student to inherit all of the methods and properties from Person
        self.age = age
        self.grade = grade

# Now, I'm adding another child, Teacher

class Teacher(Person)
    def __init__(self, fname, lname, subject, roomNo):
        super().__init__(fname, lname)
        self.subject = subject
        self.roomNo = roomNo
