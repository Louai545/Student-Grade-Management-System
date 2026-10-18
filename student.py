class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.__grades = []

    def get_grades(self):
      
      return self.__grades

    def add_grades(self, grade):
      
      self.__grades.append(grade)

    def calculate_average(self):
      if len(self.__grades)==0:
        return 0
      else :
        return round(sum(self.__grades)/len(self.__grades),2)       
      


    def calculate_grade(self):
      avg = self.calculate_average()
      if avg >= 70:
        return "A"
      elif avg >= 60:
        return "B"
      elif avg >= 50:
        return "C"
      elif avg >= 40:
        return "D"
      else :
        return "F"

           

    def display(self):
        print("student name is", self.name)
        print("student ID is", self.ID)
        print("student grades are", self.get_grades())
        print("student average grade is", self.calculate_average())
        print("student grade is", self.calculate_grade())


s1 = Student("Mohamed","S2910")

s1.add_grades(85)
s1.add_grades(90)
s1.add_grades(78)

s1.get_grades()

s1.display()