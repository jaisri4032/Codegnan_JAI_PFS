class person:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def display_basic_info(self):
        return f"Name: {self.name}\nAge: {self.age}"
class student(person):
    def __init__(self,name,age,ID, education, course):
        super().__init__(name,age)
        self.ID = ID
        self.education = education
        self.course = course
    def display_student_info(self):
        super().display_basic_info()
        print("****STUDENT DETAILS****")
        return f"Name: {self.name}\nage: {self.age}\nID: {self.ID}\neducation: {self.education}\ncourse: {self.course}"
student2 = student("jai",20,"22u41","Btech","CSE")
print(student2.display_student_info())
