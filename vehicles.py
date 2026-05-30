class Vehicle:
    def getinput(self):
        self.y=int(input("enter make year:"))
        self.m=input("enter company:")
        self.c=input("enter colour:")
    def display_info(self):
        print("company name:",self.m)
        print("manufacturing year:",self.y)
        print(" vehicle colour:",self.c)
class Car(Vehicle):
    def getcar(self):
        print("detail of car vehicle")
        super().getinput()
        self.mo=input("enter a model:")
        self.ca=int(input("enter capacity based on seats:"))
    def display_car(self):
        print("___CAR DETAIS___")
        super().display_info()
        print("car model:",self.mo)
        print("car capacity:",self.ca)
class Bike(Vehicle):
    def getbike(self):
        print("detail of bike vehicle")
        super().getinput()
        self.t=input("enter type:")
        self.m=input("enter millege:")
    def display_bike(self):
        print("___BIKE DETAIS___")
        super().display_info()
        print("bike type:",self.t)
        print("bike millege:",self.m)
v=Car()
v.getcar()
v.display_car()
w=Bike()
w.getbike()
w.display_bike()
