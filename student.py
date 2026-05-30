class Student:
    def get_input(self):
        self.name=input("Enter student name:")
        self.roll_no=input("Enter roll no:")
        self.test_m=int(input("Enter test marks::"))
    def total_marks(self):
        return self.test_m
    def display(self):
        print("Name:",self.name,"\nRoll No:",self.roll_no,"\nTest Marks:",self.test_m)
class Literary_student(Student):
    def get_input(self):
        super().get_input()
        self.lit_m=int(input("Enter literary marks:"))
    def total_marks(self):
        return self.lit_m+self.test_m
    def display(self):
        super().display()
        print("Literary Marks:",self.lit_m,"\nTotal Marks:",self.total_marks())
class sports_student(Student):
    def get_input(self):
        super().get_input()
        self.sports_m=int(input("Enter sports marks:"))
    def total_marks(self):
        return self.sports_m+self.test_m
    def display(self):
        super().display()
        print("Sports Marks:",self.sports_m,"\nTotal Marks:",self.total_marks())
class lit_sports_student(Student):
    def get_input(self):
        super().get_input()
        self.lit_m=int(input("Enter lit marks:"))
        self.sports_m=int(input("Enter sports marks:"))
    def total_marks(self):
        return self.lit_m+self.sports_m+self.test_m
    def display(self):
        super().display()
        print("Literary marks:",self.lit_m,"\nSports marks:",self.sports_m,"\nTotal Marks:",self.total_marks())
while True:
    print("\n---Student Menu---")
    print("1.Literary Student \n2.Sports Student \n3.Both \n4.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        s=Literary_student()
    elif choice==2:
        s=sports_student()
    elif choice==3:
        s=lit_sports_student()
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invalid Choice")
        continue
    s.get_input()
    print("\n---Student Details---")
    s.display()
