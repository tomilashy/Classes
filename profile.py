class profile:
  def __init__(self,name,year,semester,major,CGPA):
    self.name=name;
    self.no_of_semester=semester;
    self.year=year;
    self.major=major;
    self.cgpa=CGPA;

  def new_gpa(self,gpa):
    self.cgpa=((self.no_of_semester*self.cgpa)+gpa)/(self.no_of_semester+1)
    self.no_of_semester+=1;

  def __str__(self):
    return (f"Name: {self.name} \n Entrance Year:{self.year} \n Major: {self.major}\n CGPA:{self.cgpa} ")


