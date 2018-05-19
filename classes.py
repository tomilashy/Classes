'''
Created on May 18, 2018

@author: o_olasub
'''
class Car():
    def __init__(self,brand,year): #constructor
        self.brand=brand;       #data members
        self.year=year;
        
    def new_brand (self, brandNew):     #member function
        self.brand=brandNew;        
        
jaeho_car=Car("Hyundai",2018)       #objects
amr_care=Car("mercedes", 1999)

print (jaeho_car.brand, jaeho_car.year)

jaeho_car.new_brand("Ferrari")
print (jaeho_car.brand, jaeho_car.year)


class Rock_festival:
    def __init__(self):
        self.Vip=100;
        self.Gold=50;
        self.Regular=30;
        
    def print_(self,check):
        if check=="Vip":
            print("you have to pay ${} for Vip".format(self.Vip));
        elif check=="Regular":
             print(f"you have to pay ${self.Regular} for Regular");
        elif check=="Gold":
            print(f"you have to pay ${self.Gold} for Gold");
            

user=input("Are you a Vip,Gold or Regular member?");
user=user.capitalize()
y=input("did you pay your fees?(Yes/No)")
y=y.capitalize();

if y=="Yes":
    print("Show your ticket and you can go in ")
elif y=="No":
    info=Rock_festival();
    info.print_(user)




