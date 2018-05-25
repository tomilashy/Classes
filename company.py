
class company:
  def __init__(self,first,last,salary,title):
    self.first=first
    self.last=last
    self.salary=salary
    self.email= f"{self.first.lower()}.{self.last.lower()}@company_name.ca"

  def standard_update_class(self):
    self.salary*=1.1
    self.salary= int(self.salary)

  def __str__(self):
    return (f"Name: {self.first} {self.last} \n salary: {self.salary}\n Email:{self.email} ")

  def __mul__(self, target):
    return int(self.salary*target)

 