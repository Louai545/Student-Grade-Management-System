class Student:
    def __init__(self, name, ID, grades):
        self.name = name
        self.ID = ID
        self.grades = grades

    def display(self):
        print("student name is", self.name)
        print("student ID is", self.ID)
        print("student grade is", self.grades)


s1 = Student("Louai", 101, 90)
s1.display()