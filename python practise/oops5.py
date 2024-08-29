class Employee():
  workhours=18
  def __init__(self,aname,asalary,arole):
    self.name=aname
    self.salary=asalary
    self.role=arole
  def emp(self):
    return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
  @classmethod
  def changedworkhours(cls,newtime):##cls will take the class of the object belongs to i.e mukilan object belong to which class.=>newtime is a argument which is passed to the class variable
    cls.workhours=newtime

  @classmethod#####alternate as constructors
  def splitting(cls,string):
    
    # splitter=string.split("-")
    # return cls(splitter[0],splitter[1],splitter[2])###it gives the value to the class which the object belongs to.i.e it gives to employee class.
    ###or 
    return cls(*string.split("-"))
mukilan=Employee("Mukilan",10000,"mcemployee")
hari=Employee.splitting("hari-2500000-BE")#####after class name .the function name should be included for performing the split operation.
###after including the classmethod splitting as a constructor now we need include the functin name in the class method to object.
print(hari.emp())
