class Employee:
    def getin(self):
        self.id=input("Enter employee id:")
        self.name=input("Enter employee name:")
        self.sal=int(input("Enter employee salary:"))
        self.per=int(input("Enter bonus percentage:"))
    def calculate_bonus(self):
        self.b=self.sal*(self.per/100)
        self.bsal=self.b+self.sal
    def printemp(self):
        self.calculate_bonus()
        print("Employee ID:",self.id,"\nEmployee Name:",self.name,"\nEmployee Original Salary:",self.sal,
        "\nEmployee bonus percentage:",self.per,"\nEmployee salary with bonus:",self.bsal)
class Manager(Employee):
    def man_details(self):
        super().getin()
        self.dep=input("Enter manager department:")
        self.team=input("Enter team size:")
        self.al=input("Enter team allowance:")
    def printman(self):
        print("\n\t---Employee Details---")
        super().printemp()
        print("\n\t---Team Details---")
        print("Manager Department:",self.dep,"\nTeam Size:",self.team,"\nAllowance:",self.al)
class Developer(Employee):
    def dev_details(self):
        self.pro=input("Enter Project Name:")
        self.exp=input("Enter Project Experience:")
    def printdev(self):
        print("\n\t---Project Details---")
        print("Project name:",self.pro,"\nProject Experience:",self.exp)
m=Manager()
d=Developer()
m.man_details()
d.dev_details()
m.printman()
d.printdev()
