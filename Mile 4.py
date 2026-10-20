class Student:
  def __init__(self, name, ID, grades):
    self.name = name
    self.ID = ID
    self.grades = grades

  def display(self):
    print("student name is", self.name)
    print("student ID is", self.ID)
    print("student grade is", self.grades)

class  UndergraduateStudent(Student):
  def __init__(self,name , ID , grades , major):
    super().__init__(name,ID, grades)
    self.major = major
  
  def display_info(self):
    print("Undergraduate Student")
    super().display()
    print("Major is ", self.major)

class  GraduateStudent(Student):
  def __init__(self,name , ID , grades , program_title):
    super().__init__(name,ID, grades)
    self.program_title = program_title
  
  def display_info(self):
    print("Graduate Student")
    super().display()
    print("program title is ", self.program_title)


undergrad = UndergraduateStudent("Ahmed", "U001", 90 , "AI")
grad = GraduateStudent("Mona", "U002" , 70 , "PhD")

undergrad.display_info()
grad.display_info()