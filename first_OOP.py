#method is  afunction
#property is a variable and stores data

#funtion that returns details of student
class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("All data is saved")

    def call_details(self):
        print("Personal Details :")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, yearofgrad):
        super().__init__(name, age, gender)
        self.yearofgrad = yearofgrad

    def show_grad_date(self):
        self.call_details()
        print(f"Year of Graduation: {self.yearofgrad}")

rowan = Student('Rowan',19,'Male','2027')

rowan.show_grad_date()