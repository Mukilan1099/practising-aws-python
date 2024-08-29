###for changing the value of class variable we can use classmethod
###if we use this class method then we can change the class variables using the object itself
##writing a function so that we can cange the class variables using the object itself=>@classmethod.inside it is def.


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

mukilan=Employee("Mukilan",10000,"mcemployee")
mukilan.changedworkhours(24)
print(mukilan.workhours)
print(Employee.__dict__)####now it is changed to 24 and it is verified by this.