# class Employee:
#   workhours=18
#   pass
# mukil=Employee()
# hari=Employee()
# mukil.name="mukilan"
# mukil.salary=10000
# mukil.role="mcemployee"

# hari.name="haribhuvi"
# hari.salary=200000
# hari.role="AutomationEngineer"

###############################################################################

#instead of typing all these variables we can use constructor
# class Employee:
#   workhours=18
#   def printdetails(self):###self represents the object in which this function is called...add a near self and in f string also.
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   pass
# mukil=Employee()
# hari=Employee()
# mukil.name="mukilan"
# mukil.salary=10000########all are instance variables
# mukil.role="mcemployee"

# hari.name="haribhuvi"
# hari.salary=200000
# hari.role="AutomationEngineer"


# print(mukil.printdetails())###mukilan is self here.so self.name,and all attributes are mukilan's attributes

# ###if new argument is added inthe self,then it should be added in the object too
# print(mukil.printdetails("montycloud"))###montycloud is the new argument added in the self and it replaces the a in the function


#################################################
class Employee:
  workhours=18
  def __init__(self,aname,asalary,arole):
    self.name=aname
    self.salary=asalary
    self.role=arole
  def printdetails(self):
    return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
  pass
mukil=Employee("mukilan",10000,"mcemployee")
hari=Employee("haribhuvi",200000,"AutomationEngineer")
#####instead of typing all these variables we can use constructor...Refer the above oneand here.
####we want to pass all the variables in the object creation itself.then we use __init__ method(constructor)

print(mukil.salary)