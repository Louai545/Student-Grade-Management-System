class Student:
    def __init__(self, name, ID, grades):
    self.name = name
    self.ID = ID
    self.grades = grades
    
    def display(self):
        print(" student name is ", self.name)
        print(" student ID is ", self.ID)
        print(" student grades are ", self.grades)

        class UndergraduateStudent(Student):
            def __init__(self, name, ID, grades, major):
                super().__init__(name, ID, grades)
                self.major = major

                def display(self):
                    print("--- Undergraduate Student ---")
                    super().display()
                    print("student major is", self.major)

                    class GrdauateStudent(Student):
                        def _init__(self, name, Id, grades, program_title):
                            super().__init__(name, ID, grades)
                            self.program_title = program_title

                            def display(self):
                                print("--- Graduate Student ---")
                                      super().display()
                                      print("student program title is", self.program_title)

                                            s1 = Student("Louai", 101, 90)
                                            s1.display()
                                            print()

                                            ug = UndergraduateStudent("Louai", 101, 90, "electrical Engineering")
                                            ug.diplay()
                                            print()

                                            gr = GrdauateStudent("Ahmed", 102, 85, "MSc Power Systems")
                                              gr.display()

                    
