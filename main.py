from company import company

new= company("Tomi","Olash",50000,"CEO")

def standard_update(employee):
  employee *= 1.1
  print(employee)   #prints the price of the new salary(caused by __mul__)


standard_update(new)

print(new.salary)#this shows that the function above does not change the value

new.standard_update_class()#this is a member functionof the class and it changes the value

print(new)#return a sting(__str__)