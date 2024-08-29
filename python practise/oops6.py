##static method
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
  @classmethod
  def splitting(cls,string):
    return cls(*string.split("-"))  
  @staticmethod
  def static(string):
    print("This is a static method",string)

mukilan=Employee("Mukilan",10000,"mcemployee")
mukilan.static("hello mcha") ###it is called using the object name itself.
Employee.static("hello montycloud")###it is called using the class name itself.
###static method is accesed only inside the class(employee).....it is not accesed outside the class.