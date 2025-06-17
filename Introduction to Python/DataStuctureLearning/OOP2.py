# #Use of destructor and constructor
# class birds():
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name}'s object has been created")
#     def fly(self):
#         print(f"{self.name} is flying")
#     def sound(self):
#         print(f"{self.name} is chirping")
#     def __del__(self):
#         print(f"{self.name}'s object has now been deleted")

# parrot = birds("Tomhawk")
# parrot.fly()
# parrot.sound()

# peacock = birds("bingo")
# peacock.fly()
# parrot.sound()

# del parrot
# del peacock

class students():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show_details(self):
        print(f"Student name is {self.name}")
        print(f"Student age is {self.age}")
        print(f"Student grade is {self.grade}")
    def upd_grade(self, upd_grade):
        self.grade = upd_grade
        print(f"The new updated grade is {self.grade}")
    def __del__(self):
        print(f"{self.name}'s student record has now been deleted")

if __name__ == "__main__":
    print("Welcome to the awesome student's record creating program!")

    print("\nCreating a new student record.........")
    amalie = students("amalie", 14, "9th grade")
    print("Students details are")
    amalie.show_details()

    print("\nCreating a new student record.........")
    Jashwin = students("Jashwin", 15, "10th grade")
    print("Updating Jashwin grade....")
    Jashwin.upd_grade("11th grade")
    print("deleting jashwin record")
    Jashwin.__del__()

    print("Pre-existing objects and their instances will be deleted!")